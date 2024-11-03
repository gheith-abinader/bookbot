import os
import shutil
import markdown_blocks as mkdb
from pathlib import Path
from os import path


def copy_files_recursive(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)

def extract_title(markdown):
    for block in  mkdb.markdown_to_blocks(markdown):
        for line in block.split("\n"):
            if line.startswith("# "):
                return line[2:].strip()
        
    raise Exception("No title was found in markdown")

def generate_page(from_path, template_path, dest_path):
    print("Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = Path(from_path).read_text()
    template = Path(template_path).read_text()
    html = mkdb.markdown_to_html_node(markdown).to_html()
    print(html)
    title = extract_title(markdown)
    output_html = template.replace('{{ Title }}', title).replace('{{ Content }}', html)
    dirname = os.path.dirname(dest_path)
    if not Path(dirname).exists(): Path(dirname).mkdir(parents=True, exist_ok=True)
    if not Path(dest_path).exists: Path(dest_path).touch(mode=777)
    Path(dest_path).write_text(output_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    generate_page(os.path.join(dir_path_content, 'index.md'), template_path, os.path.join(dest_dir_path, "index.html"))
    for (dirpath, dirnames, filenames) in os.walk(dir_path_content):
        for directory in dirnames:
            generate_pages_recursive(os.path.join(dir_path_content,directory), template_path, os.path.join(dest_dir_path, directory))