from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title
import os
import os.path
import shutil

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as markdown:
        markdown_text = markdown.read()
    
    with open(template_path) as template:
        template_text = template.read()
    
    html = markdown_to_html_node(markdown_text).to_html().replace("\n"," ")
    title = extract_title(html)
    page = (
        template_text.replace("{{ Title }}", title).
        replace("{{ Content }}", html)
    )
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(page)
    
