import re

from src.textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            nodes.append(old_node)
            continue

        split = old_node.text.split(delimiter)
        if len(split) % 2 == 0:
            raise Exception(f"missing closing delimiter: {delimiter}")
        for i in range(len(split)):
            text = split[i]
            if i % 2 == 0:
                nodes.append(TextNode(text, TextType.TEXT))
            else:
                nodes.append(TextNode(text, text_type))

    return nodes


def extract_markdown_images(text):
    return re.findall(r"!\[([^\]]*)\]\(([^\)]*)\)", text)


def extract_markdown_links(text):
    return re.findall(r"\[([^\]]*)\]\(([^\)]*)\)", text)


def split_nodes_image(old_nodes):
    nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            nodes.append(old_node)
            continue

        images = extract_markdown_images(old_node.text)
        # This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)
        text = old_node.text
        for alt, link in images:
            split = text.split(f"![{alt}]({link})", 1)
            if len(split) == 0:
                continue

            nodes.append(TextNode(split[0], TextType.TEXT))
            nodes.append(TextNode(alt, TextType.IMG, link))
            if len(split[1]) > 0:
                text = split[1]

    return nodes


def split_nodes_link(old_nodes):
    nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            nodes.append(old_node)
            continue

        links = extract_markdown_links(old_node.text)
        # This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)
        text = old_node.text
        for alt, link in links:
            split = text.split(f"[{alt}]({link})", 1)
            if len(split) == 0:
                continue

            nodes.append(TextNode(split[0], TextType.TEXT))
            nodes.append(TextNode(alt, TextType.LINK, link))
            if len(split[1]) > 0:
                text = split[1]

    return nodes
