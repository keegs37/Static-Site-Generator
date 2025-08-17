import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        child1 = LeafNode("p", "first")
        child2 = LeafNode("p", "second")
        parent_node = ParentNode("div", [child1, child2])
        self.assertEqual(parent_node.to_html(), "<div><p>first</p><p>second</p></div>")

    def test_to_html_with_props(self):
        child = LeafNode("span", "child")
        parent_node = ParentNode("div", [child], props={"class": "container"})
        self.assertEqual(parent_node.to_html(), '<div class="container"><span>child</span></div>')

    def test_to_html_raises_no_tag(self):
        child = LeafNode("span", "child")
        parent_node = ParentNode(None, [child])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_raises_no_children(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_nested_parent_nodes(self):
        leaf1 = LeafNode("em", "italic")
        leaf2 = LeafNode("strong", "bold")
        inner_parent = ParentNode("span", [leaf1, leaf2])
        outer_parent = ParentNode("div", [inner_parent])
        self.assertEqual(
            outer_parent.to_html(),
            "<div><span><em>italic</em><strong>bold</strong></span></div>"
        )


if __name__ == "__main__":
    unittest.main()