import unittest
from converter import create_html_node, markdown_to_html_node
from textnode import TextNode, TextType
from htmlnode import ParentNode
from parsing import BlockType

class TestConverter(unittest.TestCase):
    def test_paragraph_conversion(self):
        block = "This is a paragraph with **bold** and _italic_ text."
        html_node = markdown_to_html_node(block)
        self.assertEqual(
            html_node.to_html(),
            "<div><p>This is a paragraph with <b>bold</b> and <i>italic</i> text.</p></div>",
            "Paragraph conversion failed!"
        )

    def test_heading_conversion(self):
        block = "## This is a **bold** heading"
        html_node = markdown_to_html_node(block)
        self.assertEqual(
            html_node.to_html(),
            "<div><h2>This is a <b>bold</b> heading</h2></div>",
            "Heading conversion failed!"
        )

    def test_code_block_conversion(self):
        block = "```def hello():\n    print(\"Hello, world!\")```"
        html_node = markdown_to_html_node(block)
        self.assertEqual(
            html_node.to_html(),
            "<div><pre><code>def hello():\n    print(\"Hello, world!\")</code></pre></div>",
            "Code block conversion failed!"
        )

    def test_blockquote_conversion(self):
        block = "> This is a blockquote with **bold** text."
        html_node = markdown_to_html_node(block)
        self.assertEqual(
            html_node.to_html(),
            "<div><blockquote>This is a blockquote with <b>bold</b> text.</blockquote></div>",
            "Blockquote conversion failed!"
        )

    def test_unordered_list_conversion(self):
        block = "- Item 1\n- Item 2\n- Item 3"
        html_node = markdown_to_html_node(block)
        self.assertEqual(
            html_node.to_html(),
            "<ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul>",
            "Unordered list conversion failed!"
        )

    def test_ordered_list_conversion(self):
        block = "1. First item\n2. Second item\n3. Third item"
        html_node = markdown_to_html_node(block)
        self.assertEqual(
            html_node.to_html(),
            "<div><ol><li>First item</li><li>Second item</li><li>Third item</li></ol>",
            "Ordered list conversion failed!</div>"
        )

    def test_paragraph_with_link(self):
        block = "This is a paragraph with a [link](https://example.com)."
        html_node = markdown_to_html_node(block)
        self.assertEqual(
            html_node.to_html(),
            '<div><p>This is a paragraph with a <a href="https://example.com">link</a>.</p></div>',
            "Paragraph with link conversion failed!"
        )


    def test_empty_block(self):
        block = ""
        html_node = markdown_to_html_node(block)
        self.assertEqual(
            html_node.to_html(),
            "<div> </div>",
            "Empty block conversion failed!"
        )

    def test_unordered_list_with_inline_formatting(self):
        block = "- **Bold Item**\n- _Italic Item_\n- `Code Item`"
        html_node = markdown_to_html_node(block)
        self.assertEqual(
            html_node.to_html(),
            "<div><ul><li><b>Bold Item</b></li><li><i>Italic Item</i></li><li><code>Code Item</code></li></ul></div>",
            "Unordered list with inline formatting conversion failed!"
        )
#do the tests

if __name__ == "__main__":
    unittest.main(verbosity=2)
