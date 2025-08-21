import unittest
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType

class TestTextToTextNodes(unittest.TestCase):
    def test_bold(self):
        text = "This is **bold** text."
        nodes = text_to_textnodes(text)
        self.assertEqual(
            nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text.", TextType.TEXT),
            ]
        )

    def test_italic(self):
        text = "This is _italic_ text."
        nodes = text_to_textnodes(text)
        self.assertEqual(
            nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" text.", TextType.TEXT),
            ]
        )

    def test_code(self):
        text = "Here is `code`."
        nodes = text_to_textnodes(text)
        self.assertEqual(
            nodes,
            [
                TextNode("Here is ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(".", TextType.TEXT),
            ]
        )

    def test_image(self):
        text = "An image: ![alt](img.png)"
        nodes = text_to_textnodes(text)
        self.assertEqual(
            nodes,
            [
                TextNode("An image: ", TextType.TEXT),
                TextNode("alt", TextType.IMAGE, "img.png"),
            ]
        )

    def test_link(self):
        text = "A [link](url.com) here."
        nodes = text_to_textnodes(text)
        self.assertEqual(
            nodes,
            [
                TextNode("A ", TextType.TEXT),
                TextNode("link", TextType.LINK, "url.com"),
                TextNode(" here.", TextType.TEXT),
            ]
        )

    def test_mixed(self):
        text = "Mix **bold** _italic_ `code` ![img](url) [link](url)"
        nodes = text_to_textnodes(text)
        self.assertEqual(
            nodes,
            [
                TextNode("Mix ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode("italic", TextType.ITALIC),
                TextNode("code", TextType.CODE),
                TextNode("img", TextType.IMAGE, "url"),
                TextNode("link", TextType.LINK, "url"),
            ]
        )

    def test_plain(self):
        text = "Just plain text."
        nodes = text_to_textnodes(text)
        self.assertEqual(
            nodes,
            [
                TextNode("Just plain text.", TextType.TEXT),
            ]
        )

    def test_complex_mixed(self):
        text = (
            "This is **text** with an _italic_ word and a `code block` and an "
            "![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        )
        nodes = text_to_textnodes(text)
        self.assertEqual(
            nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ]
        )


if __name__ == "__main__":
    unittest.main()