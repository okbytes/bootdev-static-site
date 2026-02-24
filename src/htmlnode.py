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
