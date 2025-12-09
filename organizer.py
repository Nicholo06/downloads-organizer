import os
import shutil

base_dir = r"C:/Users/USERNAME/Downloads"

extensions = {
    ".exe": "Executables",
    ".jpg": "Images",
    ".png": "Images",
    ".pdf": "Documents",
    ".zip": "Archives"
}

for filename in os.listdir(base_dir):
    file_name, file_extension = os.path.splitext(filename)

    if file_extension in extensions:
        folder_name = extensions[file_extension]

        print(f"Found {filename} -> Needs to go to {folder_name}")
    