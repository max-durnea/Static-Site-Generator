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
def split_nodes_image(old_nodes):
    resulting_nodes=[]
    for node in old_nodes:
        original_text=node.text
        links=extract_markdown_images(original_text)
        if not links:
            resulting_nodes.extend([node])
            continue
        for link in links:
            image_alt=link[0]
            image_link=link[1]
            sections = original_text.split(f"![{image_alt}]({image_link})", 1)
            textnode=TextNode(sections[0],node.text_type)
            image_node=TextNode(image_alt,TextType.IMAGE,image_link)
            original_text=sections[1]
            if(not textnode.text):
                resulting_nodes.extend([image_node])
                continue
            resulting_nodes.extend([textnode,image_node])
        if(original_text):
            resulting_nodes.extend([TextNode(original_text,TextType.TEXT)])
    return resulting_nodes
def split_nodes_link(old_nodes):
    resulting_nodes=[]
    for node in old_nodes:
        original_text=node.text
        links=extract_markdown_links(original_text)
        if not links:
            resulting_nodes.extend([node])
            continue
        for link in links:
            link_text=link[0]
            link=link[1]
            sections = original_text.split(f"[{link_text}]({link})", 1)
            textnode=TextNode(sections[0],node.text_type)
            link_node=TextNode(link_text,TextType.LINK,link)
            original_text=sections[1]
            if(not textnode.text):
                resulting_nodes.extend([link_node])
                continue
            resulting_nodes.extend([textnode,link_node])
        if(original_text):
            resulting_nodes.extend([TextNode(original_text,TextType.TEXT)])
    return resulting_nodes
def text_to_textnodes(text):
    textnode=TextNode(text,TextType.TEXT)
    result=split_nodes_delimiter([textnode],"**",TextType.BOLD)
    result=split_nodes_delimiter(result,"_",TextType.ITALIC)
    result=split_nodes_delimiter(result,"`",TextType.CODE)
    result=split_nodes_image(result)
    result=split_nodes_link(result)
    
    return result
def block_to_block_type(block):
    if(re.fullmatch(r"#{1,6}+ .*",block) is not None):
        return BlockType.HDNG
    if(re.fullmatch(r"```.*```",block) is not None):
        return BlockType.CODE
    lines = block.split("\n")
    found_type=True
    for line in lines:
        if(line[0]!='>'):
            found_type=False
            break
    if(found_type):
        return BlockType.QUOTE
    found_type=True
    for line in lines:
        if(re.fullmatch(r"- .*",line) is None):
            found_type=False
            break
    if(found_type):
        return BlockType.UNRDLST
    found_type=True
    counter=1
    for line in lines:
        format_string=rf"{counter}\. .*"
        if(re.fullmatch(format_string,line) is None):
            found_type=False
            break
        counter+=1
    if (found_type):
        return BlockType.RDLST
    return BlockType.PRGRPH

    
    




