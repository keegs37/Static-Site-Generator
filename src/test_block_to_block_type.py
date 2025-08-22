import unittest
from blocktype import BlockType, block_to_block_type
from markdown_to_blocks import markdown_to_blocks

class TestBlockToBlockType(unittest.TestCase):
    def test_code_block(self):
        md = "```\ncode here\n```"
        blocks = markdown_to_blocks(md)
        for block in blocks:
            self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_quote_block(self):
        md = "> This is a quote\n> Another quote"
        blocks = markdown_to_blocks(md)
        for block in blocks:
            self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_unordered_list_block(self):
        md = "- item 1\n- item 2\n\n- item 3\n- item 4"
        blocks = markdown_to_blocks(md)
        for block in blocks:
            self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_ordered_list_block(self):
        md = "1. item 1\n2. item 2\n\n1. item 3\n2. item 4"
        blocks = markdown_to_blocks(md)
        for block in blocks:
            self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_heading_block(self):
        md = "# Heading 1\n\n# Heading 2"
        blocks = markdown_to_blocks(md)
        for block in blocks:
            self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_paragraph_block(self):
        md = "This is a paragraph.\n\nThis is another paragraph."
        blocks = markdown_to_blocks(md)
        for block in blocks:
            self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_multiple_blocks(self):
        md = """# Heading

This is a paragraph.

- item 1
- item 2

> quote

```
code
```
"""
        expected_types = [
            BlockType.HEADING,
            BlockType.PARAGRAPH,
            BlockType.UNORDERED_LIST,
            BlockType.QUOTE,
            BlockType.CODE,
        ]
        blocks = markdown_to_blocks(md)
        self.assertEqual(len(blocks), len(expected_types))
        for block, expected in zip(blocks, expected_types):
            self.assertEqual(block_to_block_type(block), expected)

if __name__ == "__main__":
    unittest.main()