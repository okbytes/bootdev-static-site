import os
import shutil


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


def main():
    if os.path.exists("./public"):
        shutil.rmtree("./public")
    copy_content("./static", "./public")


main()
