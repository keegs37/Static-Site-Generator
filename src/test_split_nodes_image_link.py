import unittest
from unittest.mock import patch


from split_nodes_image_link import (
    split_nodes_image,
    split_nodes_link,
    TextNode,
    TextType,
)

def to_tuples(nodes):
    
    out = []
    for n in nodes:
        
        out.append((n.text, n.text_type, getattr(n, "url", None)))
    return out


class TestSplitNodesImage(unittest.TestCase):
    def test_single_image_with_text_around(self):
        node = TextNode("start ![alt](u1) end", TextType.TEXT)
        with patch("split_nodes_image_link.extract_markdown_images", return_value=[("alt", "u1")]):
            result = split_nodes_image([node])
        self.assertEqual(
            to_tuples(result),
            [
                ("start ", TextType.TEXT, None),
                ("alt", TextType.IMAGE, "u1"),
                (" end", TextType.TEXT, None),
            ],
        )

    def test_multiple_images(self):
        node = TextNode("A ![a](u1) B ![b](u2) C", TextType.TEXT)
        with patch("split_nodes_image_link.extract_markdown_images", return_value=[("a", "u1"), ("b", "u2")]):
            result = split_nodes_image([node])
        self.assertEqual(
            to_tuples(result),
            [
                ("A ", TextType.TEXT, None),
                ("a", TextType.IMAGE, "u1"),
                (" B ", TextType.TEXT, None),
                ("b", TextType.IMAGE, "u2"),
                (" C", TextType.TEXT, None),
            ],
        )

    def test_no_images_returns_single_text_node(self):
        node = TextNode("no images here", TextType.TEXT)
        with patch("split_nodes_image_link.extract_markdown_images", return_value=[]):
            result = split_nodes_image([node])
        self.assertEqual(to_tuples(result), [("no images here", TextType.TEXT, None)])

    def test_whitespace_only_node_is_skipped(self):
        node = TextNode("   \t  ", TextType.TEXT)
        # extractor should not be called; but patch anyway for safety
        with patch("split_nodes_image_link.extract_markdown_images", return_value=[("x", "y")]):
            result = split_nodes_image([node])
        self.assertEqual(result, [])

    def test_extractor_raises_appends_original_node(self):
        node = TextNode("![boom](u)", TextType.TEXT)
        with patch("split_nodes_image_link.extract_markdown_images", side_effect=Exception("bad parse")):
            result = split_nodes_image([node])
        # Original node is appended unchanged
        self.assertEqual(len(result), 1)
        self.assertIs(result[0], node)

    def test_malformed_image_markdown_treated_as_text(self):
        node = TextNode("text ![alt](not-closed text", TextType.TEXT)
        with patch("split_nodes_image_link.extract_markdown_images", return_value=[]):
            result = split_nodes_image([node])
        self.assertEqual(
            to_tuples(result),
            [("text ![alt](not-closed text", TextType.TEXT, None)],
        )


class TestSplitNodesLink(unittest.TestCase):
    def test_single_link_with_text_around(self):
        node = TextNode("hi [alt](u1) bye", TextType.TEXT)
        with patch("split_nodes_image_link.extract_markdown_links", return_value=[("alt", "u1")]):
            result = split_nodes_link([node])
        self.assertEqual(
            to_tuples(result),
            [
                ("hi ", TextType.TEXT, None),
                ("alt", TextType.LINK, "u1"),
                (" bye", TextType.TEXT, None),
            ],
        )

    def test_multiple_links(self):
        node = TextNode("A [a](u1) B [b](u2) C", TextType.TEXT)
        with patch("split_nodes_image_link.extract_markdown_links", return_value=[("a", "u1"), ("b", "u2")]):
            result = split_nodes_link([node])
        self.assertEqual(
            to_tuples(result),
            [
                ("A ", TextType.TEXT, None),
                ("a", TextType.LINK, "u1"),
                (" B ", TextType.TEXT, None),
                ("b", TextType.LINK, "u2"),
                (" C", TextType.TEXT, None),
            ],
        )

    def test_no_links_returns_single_text_node(self):
        node = TextNode("no links here", TextType.TEXT)
        with patch("split_nodes_image_link.extract_markdown_links", return_value=[]):
            result = split_nodes_link([node])
        self.assertEqual(to_tuples(result), [("no links here", TextType.TEXT, None)])

    def test_whitespace_only_node_is_skipped(self):
        node = TextNode("\n  ", TextType.TEXT)
        with patch("split_nodes_image_link.extract_markdown_links", return_value=[("x", "y")]):
            result = split_nodes_link([node])
        self.assertEqual(result, [])

    def test_extractor_raises_appends_original_node(self):
        node = TextNode("[bad](u)", TextType.TEXT)
        with patch("split_nodes_image_link.extract_markdown_links", side_effect=Exception("nope")):
            result = split_nodes_link([node])
        self.assertEqual(len(result), 1)
        self.assertIs(result[0], node)

    def test_malformed_link_markdown_treated_as_text(self):
        node = TextNode("text [alt](not-closed text", TextType.TEXT)
        with patch("split_nodes_image_link.extract_markdown_links", return_value=[]):
            result = split_nodes_link([node])
        self.assertEqual(
            to_tuples(result),
            [("text [alt](not-closed text", TextType.TEXT, None)],
        )


if __name__ == "__main__":
    unittest.main()