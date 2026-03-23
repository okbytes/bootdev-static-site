import unittest

from src.utils import extract_markdown_images, extract_markdown_links


class TestUtils(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![image2](https://i.imgur.com/bjjcJKZ.png)"
        )
        self.assertListEqual(
            [
                ("image", "https://i.imgur.com/zjjcJKZ.png"),
                ("image2", "https://i.imgur.com/bjjcJKZ.png"),
            ],
            matches,
        )

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with an [link](https://google.com) and it's not [great](https://yahoo.com)"
        )
        self.assertListEqual(
            [
                ("link", "https://google.com"),
                ("great", "https://yahoo.com"),
            ],
            matches,
        )


if __name__ == "__main__":
    unittest.main()
