from textnode import *
from htmlnode import *


def __main__():
	textnode=TextNode("Hello World",TextType.NORMAL,"https://www.google.com")
	print(textnode.__repr__())
if __name__ == "__main__":
	__main__()