from parsing import *
from textnode import *
from htmlnode import *

def create_html_node(block,block_type):
    block=block.strip('\n')
    if block_type==BlockType.PRGRPH:
        text_nodes=text_to_textnodes(block)
        return ParentNode("p",[text_node_to_html_node(text_node) for text_node in text_nodes])
    if block_type==BlockType.HDNG:
        level=block.count("#")
        text=block[level+1:]
        text = block[level + 1:].strip()
        heading_text_nodes = text_to_textnodes(text)
        return ParentNode(f"h{level}",[text_node_to_html_node(text_node) for text_node in heading_text_nodes])
    if block_type == BlockType.CODE:
        block = block[3:-3]
        return ParentNode("pre",[LeafNode("code",block)])
    if block_type == BlockType.QUOTE:
        block = block[2:]
        text_nodes = text_to_textnodes(block)
        return ParentNode("blockquote", [text_node_to_html_node(text_node) for text_node in text_nodes])
    if block_type == BlockType.UNRDLST:
        #split block into list items
        list_items = block.split("\n")
        #convert each list item into a text node
        list_items = [item[2:] for item in list_items]
        list_items = [text_to_textnodes(item) for item in list_items]
        result=[]
        for item in list_items:
            item = [text_node_to_html_node(text_node) for text_node in item]
            result.append(ParentNode("li",item))

        return ParentNode("ul", result)
    if block_type == BlockType.RDLST:
        #split block into list items
        list_items = block.split("\n")
        #remove the list identifier
        list_items = [item[3:] for item in list_items]
        #convert each list item into a text node
        list_items = [text_to_textnodes(item) for item in list_items]
        for item in list_items:
            for item1 in item:
                print(item1)
        #convert each text node into an html node, and wrap in an li node
        result = []
        for item in list_items:
            item = [text_node_to_html_node(text_node) for text_node in item]
            result.append(ParentNode("li", item))
        
        return ParentNode("ol",result)
    return None



def markdown_to_html_node(markdown):
    #split markdown into blocks:
    if not markdown:
        return LeafNode("div"," ")
    blocks=markdown_to_blocks(markdown)
    result=[]
    for block in blocks:
        block_type=block_to_block_type(block)
        html_node=create_html_node(block,block_type)
        result.append(html_node)
    return ParentNode("div",result)




        
md = "- Item 1\n- Subitem 1\n- Subitem 2\n- Item 2"
print(markdown_to_html_node(md).to_html())
# <ol><li>First item</li><li>Second item</li><li>Third item</li></ol>
