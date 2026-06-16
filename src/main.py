import os
import shutil

from markdown_blocks import markdown_to_blocks, markdown_to_html_node


def copy_content(src, dst):
    if not os.path.exists(src) or not os.path.isdir(src):
        return

    if not os.path.exists(dst):
        os.mkdir(dst)

    for path in os.listdir(src):
        new_src = os.path.join(src, path)
        new_dst = os.path.join(dst, path)

        if os.path.isdir(new_src):
            copy_content(new_src, new_dst)
        elif os.path.isfile(new_src):
            shutil.copy(new_src, new_dst)


def extract_title(markdown) -> str:
    blocks = markdown_to_blocks(markdown)
    if len(blocks) < 1:
        raise Exception("Empty markdown")
    for block in blocks:
        if block.startswith("# "):
            return block[2:]
    raise Exception("Missing h1")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        from_data = f.read()

    with open(template_path) as f:
        template_data = f.read()

    content_html = markdown_to_html_node(from_data).to_html()

    title = extract_title(from_data)

    new_html = template_data.replace("{{ Title }}", title).replace(
        "{{ Content }}", content_html
    )
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(new_html)


def main():
    if os.path.exists("public"):
        shutil.rmtree("public")
    copy_content("static", "public")

    generate_page("content/index.md", "template.html", "public/index.html")


main()
