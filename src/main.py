from textnode import TextType, TextNode
import os
from copy_static_to_public import copy_static_to_public
from generate_page import generate_page
from generate_pages_recursive import generate_pages_recursive
def main():
    public_folder = os.path.join(os.getcwd(), "public")
    static_folder = os.path.join(os.getcwd(), "static")
    copy_static_to_public(public_folder, static_folder)
   
    cd = os.getcwd()
    content_path = os.path.join(cd, "content")
    template_path = os.path.join(cd, "template.html")
    dest_path = os.path.join(cd, "public")
    generate_pages_recursive(content_path, template_path, dest_path)


if __name__ == "__main__":
    main()