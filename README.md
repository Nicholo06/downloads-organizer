# Downloads Organizer

This Python script helps you organize your Downloads folder by moving files into categorized subdirectories based on their file extensions.

## How it Works

The script iterates through all the files in your Downloads folder. For each file, it checks the file extension and moves it to a corresponding folder. For example, all `.jpg` and `.png` files are moved to the `Images` folder, and all `.pdf` and `.docx` files are moved to the `Documents` folder.

If a destination folder doesn't exist, the script will create it automatically.

## Configuration

1.  **Set your Downloads folder path:**

    Open the `organizer.py` file and modify the `base_dir` variable to point to your Downloads folder.

    ```python
    base_dir = r"C:/Users/YOUR_USERNAME/Downloads"
    ```

    Replace `YOUR_USERNAME` with your actual Windows username.

## Usage

1.  **Prerequisites:** Make sure you have Python installed on your system.

2.  **Run the script:**

    Open a terminal or command prompt, navigate to the project directory, and run the following command:

    ```bash
    python organizer.py
    ```

    The script will then start organizing your files.

## Customization

You can easily customize the script to recognize more file types.

1.  **Add new extensions:**

    Open the `organizer.py` file and add new entries to the `extensions` dictionary. The key is the file extension (e.g., `.txt`), and the value is the name of the folder where you want to move those files.

    ```python
    extensions = {
        # ... existing extensions
        ".txt": "Text Files",
        ".mp3": "Music",
    }
    ```
