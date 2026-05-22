import unittest

from src.block_markdown import BlockType, block_to_block_type, markdown_to_blocks


class TestInlineMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_blocktype_heading(self):
        blocks = block_to_block_type("# Heading")
        self.assertEqual(blocks, BlockType.HEADING)
        blocks = block_to_block_type("## Heading")
        self.assertEqual(blocks, BlockType.HEADING)
        blocks = block_to_block_type("### Heading")
        self.assertEqual(blocks, BlockType.HEADING)
        blocks = block_to_block_type("#### Heading")
        self.assertEqual(blocks, BlockType.HEADING)
        blocks = block_to_block_type("##### Heading")
        self.assertEqual(blocks, BlockType.HEADING)
        blocks = block_to_block_type("###### Heading")
        self.assertEqual(blocks, BlockType.HEADING)

    def test_block_to_blocktype_code(self):
        md = """```
def get_rekt():
    pass
def ok():
    print("ok")
```"""
        blocks = block_to_block_type(md)
        self.assertEqual(blocks, BlockType.CODE)

    def test_block_to_blocktype_quote(self):
        md = """> Four score and seven years ago,
> I dunno. WAR."""
        blocks = block_to_block_type(md)
        self.assertEqual(blocks, BlockType.QUOTE)

    def test_block_to_blocktype_unordered(self):
        md = """- eggs
- milk
- flour
- bread"""
        blocks = block_to_block_type(md)
        self.assertEqual(blocks, BlockType.UNORDERED_LIST)

    def test_block_to_blocktype_ordered(self):
        md = """1. Steal socks
2. ???
3. Profit"""
        blocks = block_to_block_type(md)
        self.assertEqual(blocks, BlockType.ORDERED_LIST)

    def test_block_to_blocktype_paragraph(self):
        blocks = block_to_block_type("####### Heading")
        self.assertEqual(blocks, BlockType.PARAGRAPH)
        blocks = block_to_block_type("#$ Heading")
        self.assertEqual(blocks, BlockType.PARAGRAPH)
        blocks = block_to_block_type("""
        1. Steal socks
        2. ???
        3. Profit""")
        self.assertEqual(blocks, BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()
