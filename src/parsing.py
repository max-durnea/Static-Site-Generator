from htmlnode import *
from textnode import *
import re
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    TextNodeList = []
    for node in old_nodes:
        inside_delimiters=False
        split_text = node.text.split(delimiter)
        if(len(split_text)%2==0):
            raise ValueError("Wrong Format!")
        for text in split_text:
            if inside_delimiters:
                TextNodeList.append(TextNode(text,text_type,node.url))
            else:
                TextNodeList.append(TextNode(text,node.text_type,node.url))
            inside_delimiters=not inside_delimiters
        
    return TextNodeList
def extract_markdown_images(text):
    matches=re.findall(r"!\[([\w ]+)\]\((.+?)\)",text)
    return matches
def extract_markdown_links(text):
    matches=re.findall(r"\[([\w ]+)\]\((.+?)\)",text)
    return matches

