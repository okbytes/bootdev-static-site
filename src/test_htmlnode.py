import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_defaults_none(self):
        node = HTMLNode()
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_partial(self):
        node = HTMLNode(tag="p", children="some text")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, "some text")
        self.assertEqual(node.props, None)

    def test_props(self):
        node = HTMLNode(tag="p", children="some text", props={ "href": "google.com" })
        self.assertEqual(node.props_to_html(), ' href="google.com"')

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Learn more", { "href": "wikipedia.org"})
        self.assertEqual(node.to_html(), '<a href="wikipedia.org">Learn more</a>')

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_many_children(self):
        parent_node = ParentNode(
            "div",
            [
                ParentNode(
                    "span",
                    [
                        LeafNode("b", "grandchild"),
                        LeafNode("b", "grandchild")
                    ]
                ),
                ParentNode(
                    "span",
                    [
                        LeafNode("b", "grandchild"),
                        LeafNode("b", "grandchild")
                    ]
                )
            ]
        )
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b><b>grandchild</b></span><span><b>grandchild</b><b>grandchild</b></span></div>",
        )

    def test_to_html_with_lots_of_children(self):
            parent_node = ParentNode(
                "div",
                [
                    ParentNode(
                        "span",
                        [
                            ParentNode("em",[LeafNode("b", "grandchild")]),
                            LeafNode("b", "grandchild")
                        ]
                    ),
                    ParentNode(
                        "span",
                        [
                            LeafNode("b", "grandchild"),
                            ParentNode("em",[LeafNode("b", "grandchild")]),
                        ]
                    )
                ]
            )
            self.assertEqual(
                parent_node.to_html(),
                "<div><span><em><b>grandchild</b></em><b>grandchild</b></span><span><b>grandchild</b><em><b>grandchild</b></em></span></div>",
            )

if __name__ == "__main__":
    unittest.main()
