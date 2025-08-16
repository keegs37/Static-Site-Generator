from htmlnode import HTMLNode
import unittest

def test_htmlnode():
    node = HtmlNode("This is a HTML node", "div", {"class": "test"})
    node2 =HtmlNode("This is a HTML node", "div", {"class": "test"})
    self.assertEqual(node, node2)

def test_htmlnode_not_eq(self):
    node = HtmlNode("This is a HTML node", "div", {"class": "test"})
    node2 = HtmlNode("This is a different HTML node", "span", {"class": "test"})
    self.assertNotEqual(node, node2)

def test_htmlnode_repr(self):
    node = HtmlNode("This is a HTML node", "div", {"class": "test"})
    expected_repr = "HtmlNode(This is a HTML node, div, {'class': 'test'})"
    self.assertEqual(repr(node), expected_repr)

if __name__ == "__main__":
    unittest.main()