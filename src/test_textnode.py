import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):

    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2, "Test failed: Text nodes with same content and type should be equal!")

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.__repr__(), "TextNode(This is a text node,Bold text,None)", "Test failed: __repr__ output doesn't match expected.")

    def test_different(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.NORMAL)
        self.assertNotEqual(node, node2, "Test failed: Text nodes with different types should not be equal!")

    def test_empty_text(self):
        node = TextNode("", TextType.NORMAL)
        self.assertEqual(node.text, "", "Test failed: Empty text node should have an empty string as text!")

    def test_different_text(self):
        node1 = TextNode("Hello", TextType.BOLD)
        node2 = TextNode("Goodbye", TextType.BOLD)
        self.assertNotEqual(node1, node2, "Test failed: Text nodes with different content should not be equal!")

    def test_different_text_type(self):
        node1 = TextNode("Sample", TextType.BOLD)
        node2 = TextNode("Sample", TextType.ITALIC)
        self.assertNotEqual(node1, node2, "Test failed: Text nodes with different types should not be equal!")

    def test_none_values(self):
        node = TextNode(None, TextType.NORMAL)
        self.assertIsNone(node.text, "Test failed: Text node with None should result in None as text!")

# Run tests with verbosity=2 for more detailed output
if __name__ == "__main__":
    unittest.main(verbosity=2)
