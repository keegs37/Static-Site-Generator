from generate_page import generate_page
import os

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath="/"):
    content = os.listdir(dir_path_content)

    for item in content:
        src = os.path.join(dir_path_content, item)
        dest = os.path.join(dest_dir_path, item)

        if os.path.isfile(src):
            md_to_htmL_file = dest.replace(".md", ".html")
            generate_page(src, template_path, md_to_htmL_file, basepath)
        else:
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            generate_pages_recursive(src, template_path, dest)

