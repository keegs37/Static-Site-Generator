def extract_title(markdown):
    heading_start = markdown.find("<h1>")
    heading_end = markdown.find("</h1>", heading_start + 1)
    if heading_start == -1:
        raise Exception("Title not found")
    
    return markdown[heading_start + 4 :heading_end].strip()


