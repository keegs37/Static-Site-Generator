from textnode import TextType, TextNode
import os
from copy_static_to_public import copy_static_to_public
def main():
    public_folder = os.path.join(os.getcwd(), "public")
    static_folder = os.path.join(os.getcwd(), "static")
    copy_static_to_public(public_folder, static_folder)
    


if __name__ == "__main__":
    main()