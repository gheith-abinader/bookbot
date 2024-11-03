import os
import shutil

from copystatic import copy_files_recursive, generate_pages_recursive


dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)
    
    template_path = os.path.join(os.getcwd(), "template.html")
    generate_pages_recursive(dir_path_content=dir_path_content ,template_path=template_path,dest_dir_path=dir_path_public)


main()
