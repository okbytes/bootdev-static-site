import unittest

from src.main import extract_title


class TestMain(unittest.TestCase):
    def test_extract_title(self):
        self.assertEqual(
            extract_title("""
# Hello
"""),
            "Hello",
        )

        self.assertEqual(
            extract_title("""
# Hey

What's up?
"""),
            "Hey",
        )

        self.assertEqual(
            extract_title("""
What's up?

# Nothing

Wild.
"""),
            "Nothing",
        )


if __name__ == "__main__":
    unittest.main()
