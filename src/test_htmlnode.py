import unittest

from htmlnode import HTMLNode


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

if __name__ == "__main__":
    unittest.main()
