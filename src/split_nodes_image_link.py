from extract_markdown_links_and_images import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType
import re

# [
#     TextNode("This is text with a link ", TextType.TEXT),
#     TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
#     TextNode(" and ", TextType.TEXT),
#     TextNode(
#         "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
#     ),
# ]
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
        tokens = re.split(r'\![^\]]+\]\([^\)]+\)', node.text)
       
        for i in range(len(tokens)):
            if not tokens[i].strip() and i < len(image):
                new_nodes.append(TextNode(image[i][0], TextType.IMAGE, image[i][1]))
                
            elif tokens[i].strip():
                new_nodes.append(TextNode(tokens[i], TextType.TEXT))
                if i < len(image):
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
   
    


#node = TextNode(
    "test [image](https://i.imgur.com/zjjcJKZ.png) test this cool  ![image](https://i.imgur.com/zjjcJKZ.png) and ![image](https://i.imgur.com/zjjcJKZ.png) and another",
    TextType.TEXT,
#)
#new_nodes = split_nodes_image([node])

node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT,
)
new_nodes = split_nodes_link([node])
print(new_nodes)