import os
import shutil

# Ask user for folder path
folder_path = input("Enter folder path: ")

# Check if folder exists
if not os.path.exists(folder_path):
    print("Folder does not exist.")
    exit()

# Define file categories and extensions
file_categories = {
    "images": [".jpg", ".jpeg", ".png", ".gif"],
    "documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "music": [".mp3", ".wav"],
    "videos": [".mp4", ".mkv", ".avi"],
    "code": [".py", ".js", ".html", ".css"],
    "archives": [".zip", ".rar"]
}

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    # Skip directories, process only files
    if os.path.isfile(file_path):
        _, extension = os.path.splitext(filename)
        moved = False

        # Check file extension and match with category
        for category, extensions in file_categories.items():
            if extension.lower() in extensions:
                category_folder = os.path.join(folder_path, category)

                # Create folder if it does not exist
                if not os.path.exists(category_folder):
                    os.makedirs(category_folder)

                # Move file to appropriate folder
                shutil.move(file_path, os.path.join(category_folder, filename))
                print(f"Moved {filename} to {category}/")
                moved = True
                break

        # If file type is unknown, move to 'others'
        if not moved:
            other_folder = os.path.join(folder_path, "others")

            if not os.path.exists(other_folder):
                os.makedirs(other_folder)

            shutil.move(file_path, os.path.join(other_folder, filename))
            print(f"Moved {filename} to others/")

print("Sorting completed.")