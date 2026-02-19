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
