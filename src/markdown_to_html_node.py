from markdown_to_blocks import markdown_to_blocks
from blocktype import block_to_block_type
from htmlnode import HTMLNode
from leafnode import LeafNode
from text_to_textnodes import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType
from parentnode import ParentNode

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block).value

        if block_type == "paragraph":
            html_paragraph = paragraph_block_to_html(block)
            block_nodes.append(html_paragraph)
            
        elif block_type == "heading":
            html_heading = heading_block_to_html(block)
            block_nodes.append(html_heading)

        elif block_type == "code":
            html_code = code_block_to_html(block)
            block_nodes.append(html_code)

        elif block_type == "quote":
            html_quote = quote_block_to_html(block)
            block_nodes.append(html_quote)

        elif block_type == "unordered list":
            html_unordered_list = unordered_list_block_to_html(block)
            block_nodes.append(html_unordered_list)

        elif block_type == "ordered list":
            html_ordered_list = ordered_list_block_to_html(block)
            block_nodes.append(html_ordered_list)
    
    div_node = ParentNode("div", block_nodes)

    return div_node

def text_to_children(text, markdown_tag=""):
    text_nodes = text_to_textnodes(text)
    child_nodes = []
    for node in text_nodes:
        # Remove markdown tags from the html output
        if node.text.startswith(markdown_tag):
            node.text = node.text.replace(markdown_tag, "", 1)
        
        # Remove markdown code tags from html output
        if node.text_type == "code":
            node.text = node.text.replace(markdown_tag, "")
        child_nodes.append(text_node_to_html_node(node))
    return child_nodes

def paragraph_block_to_html(paragraph_block):
    children_nodes = text_to_children(paragraph_block)
    html_paragraph_node = ParentNode("p", children_nodes)
    return html_paragraph_node

def heading_block_to_html(html_block, markdown_tag="# "):
    children_nodes = text_to_children(html_block, markdown_tag)
    html_heading_node = ParentNode("h1", children_nodes)
    return html_heading_node

def code_block_to_html(code_block):
    text_node = TextNode(code_block, TextType.TEXT)
    text_node.text = text_node.text.strip()
    text_node.text = text_node.text.replace("```", "")
    child_node = text_node_to_html_node(text_node)
    html_code_node = ParentNode("codeblock", [child_node])
    return html_code_node

def quote_block_to_html(quote_block, markdown_tag="> "):
    children_nodes = text_to_children(quote_block, markdown_tag)
    html_quote_node = ParentNode("blockquote", children_nodes)
    return html_quote_node

def unordered_list_block_to_html(unordered_list_block, markdown_tag="- "):
    lines = [line.strip() for line in unordered_list_block.split('\n') if line.strip()]
    li_nodes = []
    for line in lines:
        # Remove the "- " marker
        if line.startswith(markdown_tag):
            item_text = line[len(markdown_tag):]
        else:
            item_text = line
        children = text_to_children(item_text)
        li_nodes.append(ParentNode("li", children))
    html_unordered_list_node = ParentNode("ul", li_nodes)
    return html_unordered_list_node

def ordered_list_block_to_html(ordered_list_block):
    lines = [line.strip() for line in ordered_list_block.split('\n') if line.strip()]
    li_nodes = []
    for line in lines:
        # Remove the "1. ", "2. ", etc. marker
        if ". " in line:
            item_text = line.split(". ", 1)[1]
        else:
            item_text = line
        children = text_to_children(item_text)
        li_nodes.append(ParentNode("li", children))
    html_ordered_list_node = ParentNode("ol", li_nodes)
    return html_ordered_list_node
