'''
text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
print(extract_markdown_images(text))
# [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
'''
import re
def extract_markdown_images(text):
    extracted_images = []
    alt_text_matches = re.findall(r"(?<=\[)[^\]]+(?=\])", text)
    url_matches = re.findall(r"(?<=\()[^\)]+(?=\))", text)
    if not alt_text_matches:
        raise Exception("Text does not contain image(s)")
    for i in range(len(alt_text_matches)):
        image = (alt_text_matches[i], url_matches[i])
        extracted_images.append(image)

    return(extracted_images)

        

extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")

def extract_markdown_links(text):
    extracted_links = []
    link_text_matches = re.findall(r"(?<=\[)[^\]]+(?=\])", text)
    url_matches = re.findall(r"(?<=\()[^\)]+(?=\))", text)
    if not link_text_matches:
        raise Exception("Text does not contain image(s)")
    for i in range(len(link_text_matches)):
        image = (link_text_matches[i], url_matches[i])
        extracted_links.append(image)

    return(extracted_links)

extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")