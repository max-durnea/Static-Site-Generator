import unittest
from textnode import TextNode, TextType
from parsing import *

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
    def test_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        node1 = TextNode("This is text with a **bold block** word",TextType.TEXT)
        new_nodes=split_nodes_delimiter(split_nodes_delimiter([node,node1], "`", TextType.CODE),"**",TextType.BOLD)
        sample=[TextNode("This is text with a ",TextType.TEXT,None), TextNode("code block",TextType.CODE,None), TextNode(" word",TextType.TEXT,None), TextNode("This is text with a ",TextType.TEXT,None), TextNode("bold block",TextType.BOLD,None), TextNode(" word",TextType.TEXT,None)]
        for i in range(0,len(new_nodes)):
            self.assertEqual(sample[i],new_nodes[i],"Test failed: Parsing Done Wrong!")
    def test_img_extract(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]
        extracted_result = extract_markdown_images(text)
        self.assertEqual(extracted_result, result, "Test failed: Image data extracted wrong")
    def test_link_extract(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        result = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        extracted_result = extract_markdown_links(text)
        self.assertEqual(extracted_result,result,"Test failed: Link data extracted wrong")

# Run tests with verbosity=2 for more detailed output
if __name__ == "__main__":
    unittest.main(verbosity=2)
