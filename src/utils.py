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


def extract_markdown_images():
    pass
