import re
def extract_markdown_images(text):
    extracted_images = []
    alt_text_matches = re.findall(r"(?<=\!\[)[^\]]+(?=\])", text)
    url_matches = re.findall(r"(?<=\()[^\)]+(?=\))", text)
    if not alt_text_matches:
        raise Exception("Text does not contain image(s)")
    for i in range(len(alt_text_matches)):
        image = (alt_text_matches[i], url_matches[i])
        extracted_images.append(image)

    return(extracted_images)

        



def extract_markdown_links(text):
    extracted_links = []
    link_text_matches = re.findall(r"(?<=\[)[^\]]+(?=\])", text)
    url_matches = re.findall(r"(?<=\()[^\)]+(?=\))", text)
    if not link_text_matches:
        raise Exception("Text does not contain link(s)")
    for i in range(len(link_text_matches)):
        link = (link_text_matches[i], url_matches[i])
        extracted_links.append(link)

    return(extracted_links)

