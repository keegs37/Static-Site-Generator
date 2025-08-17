from htmlnode import HTMLNode
import unittest

class TestHTMLNode(unittest.TestCase):
    def test_htmlnode(self):
        node = HTMLNode("div", "This is a HTML node", None, {"class": "test"})
        node2 = HTMLNode("div", "This is a HTML node", None, {"class": "test"})
        self.assertEqual(node, node2)

    def test_htmlnode_not_eq(self):
        node = HTMLNode("div", "This is a HTML node", None, {"class": "test"})
        node2 = HTMLNode("span", "This is a different HTML node", None, {"class": "test"})
        self.assertNotEqual(node, node2)

    def test_htmlnode_repr(self):
        node = HTMLNode("div", "This is a HTML node", None, {"class": "test"})
        expected_repr = "HTMLNode(div, This is a HTML node, None, {'class': 'test'})"
        self.assertEqual(repr(node), expected_repr)


if __name__ == "__main__":
    unittest.main()