import os
import sys


def rename_bandcamp_directory_files(dir_path):
    if not os.path.isdir(dir_path):
        print(f"path '{dir_path}' no exist")
        return

    for root, _, files in os.walk(dir_path):
        for file in files:
            # be better this is so dumb. this hyperspecififc to bandcamp downloads
            if ' - 0' not in file:
                continue

            old_file_path = os.path.join(root, file)
            new_file_name = '0' +file.split(' - 0', 1)[1]
            new_file_path = os.path.join(root, new_file_name)

            if old_file_path != new_file_path:
                print(f"renaming  to '{new_file_path}'")
                os.rename(old_file_path, new_file_path)


def main():
    if len(sys.argv) < 2:
        #create album folder in proj directory with files to rename for arg
        print("do python scrip.py <album_dir_path>")
        return

    rename_bandcamp_directory_files(sys.argv[1])

if __name__ == "__main__":
    main()