import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is text", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_bold(self):
        node = TextNode("This is text", TextType.BOLD)
        node2 = TextNode("This is text", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_default_url(self):
        node = TextNode("This is text", TextType.BOLD)
        self.assertEqual(node.url, None)

    def test_eq_urls(self):
        node = TextNode("This is text", TextType.BOLD, "google.com")
        node2 = TextNode("This is text", TextType.TEXT, "google.com")
        self.assertNotEqual(node, node2)
        self.assertEqual(node.url, node.url)


if __name__ == "__main__":
    unittest.main()
