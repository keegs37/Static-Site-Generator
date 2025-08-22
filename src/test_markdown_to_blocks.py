import unittest
from markdown_to_blocks import markdown_to_blocks

class Test_markdown_to_blocks(unittest.TestCase):
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

    def test_single_paragraph(self):
        md = "Just a single paragraph."
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Just a single paragraph."])

    def test_multiple_empty_lines(self):
        md = """
First block


Second block



Third block
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "First block",
                "Second block",
                "Third block",
            ],
        )

    def test_leading_and_trailing_whitespace(self):
        md = """

    Block with leading and trailing whitespace    

"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            ["Block with leading and trailing whitespace"],
        )

    def test_only_newlines(self):
        md = "\n\n\n"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [""])

    def test_mixed_content(self):
        md = """
# Heading

Paragraph text

- List item 1
- List item 2

Another paragraph
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "# Heading",
                "Paragraph text",
                "- List item 1\n- List item 2",
                "Another paragraph",
            ],
        )

if __name__ == "__main__":
    unittest.main()