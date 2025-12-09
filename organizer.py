import os
import shutil

base_dir = r"C:/Users/USERNAME/Downloads"

extensions = {
    ".exe": "Executables",
    ".jpg": "Images",
    ".png": "Images",
    ".webp": "Images",
    ".svg": "Images",
    ".jpeg": "Images",
    ".pdf": "Documents",
    ".docx": "Documents",
    ".doc": "Documents",
    ".xls": "Documents",
    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    ".gz": "Archives",
    ".iso": "ISO",
    ".msi": "Executables",
    ".mp4": "Videos",
    ".mov": "Videos",
    ".srt": "Subtitles",
    ".blend": "Blender Files",
    ".html": "HTML",
    ".torrent": "Torrent",
    ".txt": "Text Files",
    ".sql": "SQL",
    ".py": "Python Files",
    ".db": "Database",
    ".xlsx": "Documents",
    ".pptx": "Documents",
    ".js": "Javascript",
    ".bin": "Bin Files",
    ".json": "JSON Files",
    ".crdownload": "CRDOWNLOAD",
    ".php": "PHP"
}

for filename in os.listdir(base_dir):
    file_name, file_extension = os.path.splitext(filename)
    file_extension = file_extension.lower()

    if file_extension in extensions:
        folder_name = extensions[file_extension]
        source = os.path.join(base_dir, filename)
        destination_folder = os.path.join(base_dir, folder_name)
        os.makedirs(destination_folder, exist_ok=True)
        shutil.move(source, destination_folder)


        print(f"Processing: {filename}")
    