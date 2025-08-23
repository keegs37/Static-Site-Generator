import unittest
from markdown_to_html_node import markdown_to_html_node

class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_paragraph(self):
        md = "This is a paragraph."
        html = markdown_to_html_node(md)
        self.assertIn("<p>", html)
        self.assertIn("This is a paragraph.", html)
        self.assertIn("</p>", html)

    def test_bold_and_italic(self):
        md = "This is **bold** and _italic_ text."
        html = markdown_to_html_node(md)
        self.assertIn("<b>bold</b>", html)
        self.assertIn("<i>italic</i>", html)

    def test_code_inline(self):
        md = "Here is `code`."
        html = markdown_to_html_node(md)
        self.assertIn("<code>code</code>", html)

    def test_heading(self):
        md = "# Heading"
        html = markdown_to_html_node(md)
        self.assertIn("<h1>", html)
        self.assertIn("Heading", html)
        self.assertIn("</h1>", html)

    def test_code_block(self):
        md = "```\ncode block\n```"
        html = markdown_to_html_node(md)
        self.assertIn("<codeblock>", html)
        self.assertIn("code block", html)
        self.assertIn("</codeblock>", html)

    def test_quote(self):
        md = "> quoted text"
        html = markdown_to_html_node(md)
        self.assertIn("<blockquote>", html)
        self.assertIn("quoted text", html)
        self.assertIn("</blockquote>", html)

    def test_unordered_list(self):
        md = "- item 1\n- item 2"
        html = markdown_to_html_node(md)
        self.assertIn("<ul>", html)
        self.assertIn("<li>", html)  # If your implementation uses <li>
        self.assertIn("item 1", html)
        self.assertIn("item 2", html)
        self.assertIn("</ul>", html)

    def test_ordered_list(self):
        md = "1. first\n2. second"
        html = markdown_to_html_node(md)
        self.assertIn("<ol>", html)
        self.assertIn("<li>", html)  # If your implementation uses <li>
        self.assertIn("first", html)
        self.assertIn("second", html)
        self.assertIn("</ol>", html)

    def test_multiple_blocks(self):
        md = "# Heading\n\nParagraph text.\n\n- item 1\n- item 2\n\n1. first\n2. second"
        html = markdown_to_html_node(md)
        self.assertIn("<h1>", html)
        self.assertIn("<p>", html)
        self.assertIn("<ul>", html)
        self.assertIn("<ol>", html)

if __name__ == "__main__":
    unittest.main()