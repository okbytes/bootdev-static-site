import unittest

from src.inline_markdown import split_nodes_delimiter
from src.textnode import TextNode, TextType


class TestMarkdown(unittest.TestCase):
    def test_simple_code(self):
        node = TextNode("A word `code block` more word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("A word ", TextType.TEXT, None),
                TextNode("code block", TextType.CODE, None),
                TextNode(" more word", TextType.TEXT, None),
            ],
        )

    def test_simple_bold(self):
        node = TextNode("A word **bold block** more word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("A word ", TextType.TEXT, None),
                TextNode("bold block", TextType.BOLD, None),
                TextNode(" more word", TextType.TEXT, None),
            ],
        )

    def test_simple_italic(self):
        node = TextNode("A word _italic block_ more word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(
            new_nodes,
            [
                TextNode("A word ", TextType.TEXT, None),
                TextNode("italic block", TextType.ITALIC, None),
                TextNode(" more word", TextType.TEXT, None),
            ],
        )

    def test_tricky_bold(self):
        node = TextNode("**Bold block** more word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("Bold block", TextType.BOLD, None),
                TextNode(" more word", TextType.TEXT, None),
            ],
        )


if __name__ == "__main__":
    unittest.main()
