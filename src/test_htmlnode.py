import unittest
from htmlnode import *
from textnode import *
class TestHTMLNode(unittest.TestCase):
	def test_eq(self):
		node = HTMLNode("p", "This is a paragraph")
		node2 = HTMLNode("p", "This is a paragraph")
		self.assertEqual(node.__repr__(), node2.__repr__(), f"Test failed: HTML nodes with same tag and value should be equal!\n{node.__repr__()} {node2.__repr__()}")
	def test_repr(self):
		node = HTMLNode("p", "This is a paragraph")
		self.assertEqual(node.__repr__(), "HTMLNode(p,This is a paragraph,None,None)", f"Test failed: __repr__ output doesn't match expected.\n{node.__repr__()}")
	def test_different(self):
		node = HTMLNode("p", "This is a paragraph")
		node2 = HTMLNode("div", "This is a paragraph")
		self.assertNotEqual(node, node2, "Test failed: HTML nodes with different tags should not be equal!")
	def test_empty_tag(self):
		node = HTMLNode("", "This is a paragraph")
		self.assertEqual(node.tag, "", "Test failed: Empty tag should result in empty string!")
	def test_props(self):
		node = HTMLNode("href", "This is a paragraph", props={"href":"https://www.google.com"})
		self.assertEqual(node.props_to_html(), 'href="https://www.google.com"', "Test failed: props_to_html output doesn't match expected.")
	def test_leaf_node(self):
		node = LeafNode("a", "This is a paragraph", props={"href":"https://www.google.com"})
		self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">This is a paragraph</a>", "Test failed: LeafNode to_html output doesn't match expected.")
	def test_leaf_node_only_value(self):
		node = LeafNode(value="This is a paragraph")
		self.assertEqual(node.to_html(), "This is a paragraph", "Test failed: LeafNode to_html output doesn't match expected.")
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
	def test_text(self):
		node = TextNode("This is a text node", TextType.TEXT)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, None)
		self.assertEqual(html_node.value, "This is a text node")
if __name__ == "__main__":
    unittest.main(verbosity=2)