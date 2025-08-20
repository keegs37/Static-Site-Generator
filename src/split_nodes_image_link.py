from extract_markdown_links_and_images import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType
import re

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text.isspace():
            continue
        try:
            image = extract_markdown_images(node.text)
        except Exception:
            new_nodes.append(node)
            continue

        image = extract_markdown_images(node.text)
        tokens = re.split(r'\![^\]]+\]\([^\)]+\)', node.text) # Regex splits on the markdown image syntax, leaving just the remaining text
       
        
        for i in range(len(tokens)): # The length of tokens will always be the same or more than the length of image
            if not tokens[i].strip() and i < len(image): # If tokens[i] is whitespace and there is an image available to append
                new_nodes.append(TextNode(image[i][0], TextType.IMAGE, image[i][1]))
                
            elif tokens[i].strip():
                new_nodes.append(TextNode(tokens[i], TextType.TEXT))
                if i < len(image): # Make sure there is an image to append before appending 
                    new_nodes.append(TextNode(image[i][0], TextType.IMAGE, image[i][1]))


    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:

        if node.text.isspace():
            continue
        try:
            link = extract_markdown_links(node.text)
        except Exception:
            new_nodes.append(node)
            continue

        link = extract_markdown_links(node.text)
        tokens = re.split(r'\[[^\]]+\]\([^\)]+\)', node.text)
    
        for i in range(len(tokens)):
            if not tokens[i].strip() and i < len(link):
                new_nodes.append(TextNode(link[i][0], TextType.LINK, link[i][1]))
                
            elif tokens[i].strip():
                new_nodes.append(TextNode(tokens[i], TextType.TEXT))
                if i < len(link):
                    new_nodes.append(TextNode(link[i][0], TextType.LINK, link[i][1]))


    return new_nodes
   
