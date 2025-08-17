from leafnode import LeafNode
import unittest

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_p_not_eq(self):
        node = LeafNode("p", "Hello, world")
        node_2 = LeafNode("div", "Hello, world")
        self.assertNotEqual(node, node_2)

    def test_leaf_to_html_a_eq(self):
        node = LeafNode("a", "Click me!", {"href": "https://boot.dev"})
        self.assertEqual(node.to_html(), '<a href="https://boot.dev">Click me!</a>')
    
    def test_leaf_to_html_a_not_eq(self):
        node = LeafNode("a", "Click me!", {"href": "https://boot.dev"})
        node_2 = LeafNode("div", "Click me!", {"href": "https://boot.dev"})
        self.assertNotEqual(node, node_2)
if __name__ == "__main__":
    unittest.main()