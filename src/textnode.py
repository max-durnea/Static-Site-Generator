from enum import Enum

class TextType(Enum):
	BOLD = "Bold text"
	ITALIC = "Italic text"
	CODE = "Code text"
	LINK = "Link"
	IMAGE = "Image"
	TEXT = "Text"
	NORMAL = "Normal text"
class TextNode:
	def __init__(self,text,text_type,url=None):
		self.text = text
		self.text_type = text_type
		self.url = url
	def __eq__(self,other):
		return self.text == other.text and self.text_type == other.text_type and self.url == other.url
	def __repr__(self):
		return f"TextNode({self.text},{self.text_type.value},{self.url})"
def markdown_to_blocks(markdown):
	return [item.strip() for item in markdown.split("\n\n")]
md="""
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
print(markdown_to_blocks(md))
    