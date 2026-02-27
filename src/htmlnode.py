from src.textnode import TextNode, TextType


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def props_to_html(self):
        if self.props is None:
            return ""

        str = ""
        for prop in self.props:
            str += f' {prop}="{self.props[prop]}"'
        return str

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props_to_html()})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag or None, value, None, props)

    def __repr__(self):
        return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props_to_html()})"

    def to_html(self):
        if not self.value:
            raise ValueError("leaf nodes must have a value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html() if self.props else ''}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def __repr__(self):
      return f"ParentNode(tag={self.tag}, children={self.value}, props={self.props_to_html()})"

    def to_html(self):
        if not self.tag:
            raise ValueError("parent nodes must have a tag")
        if not self.children:
            raise ValueError("parent nodes must have children")

        str = f"<{self.tag}{self.props_to_html() if self.props else ''}>"
        for child in self.children:
            str += child.to_html()
        str += f"</{self.tag}>"
        return str

def text_node_to_html_node(text_node: TextNode):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(tag=None, value=text_node.text)
        case TextType.BOLD:
            return LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag="code", value=text_node.text)
        case TextType.LINK:
            return LeafNode(
                tag="a",
                value=text_node.text,
                props={ "href": text_node.url}
            )
        case TextType.IMG:
            return LeafNode(
                tag="img",
                value=None,
                props={
                    "src": text_node.url,
                    "alt": text_node.text
                }
            )
        case _:
            raise Exception("invalid text_type")
