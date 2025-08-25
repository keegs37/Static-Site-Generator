from textnode import TextType, TextNode
import os
from copy_static_to_public import copy_static_to_public
from generate_page import generate_page
def main():
    public_folder = os.path.join(os.getcwd(), "public")
    static_folder = os.path.join(os.getcwd(), "static")
    copy_static_to_public(public_folder, static_folder)

    cd = os.getcwd()
    from_path = os.path.join(cd, "content/index.md")
    template = os.path.join(cd, "template.html")
    dest_path = os.path.join(cd, "public/index.html")
    generate_page(from_path, template, dest_path)
    


if __name__ == "__main__":
    main()