import os
import shutil

# Path of the desktop folder
desktop_path = os.path.expanduser("~/Desktop")
#print('desktop path:', desktop_path)

# Dictionary containing the folder names and their corresponding file extensions
# Not all file extensions have been listed. I consider .ppt and .xls as document extensions
folders = {
    "Images": [".jpeg", ".jpg", ".png", ".gif"],
    "Documents": [".doc", ".docx", ".pdf", ".txt"],
    "Archives": [".zip", ".rar"]
}

# Create the subfolders if they don't exist
for folder_name in folders:
    folder_path = os.path.join(desktop_path, folder_name)
    if not os.path.exists(folder_path):
        os.mkdirs(folder_path)

# Move files to the corresponding subfolder
for file_name in os.listdir(desktop_path):
    original_file_path = os.path.join(desktop_path, file_name)
    if os.path.isfile(original_file_path):
        for folder_name, extensions in folders.items():
            for extension in extensions:
                if file_name.endswith(extension):
                    destination_folder = os.path.join(desktop_path, folder_name)
                    shutil.move(file_path, destination_folder)
