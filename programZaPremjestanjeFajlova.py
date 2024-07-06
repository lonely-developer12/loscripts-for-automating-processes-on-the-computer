import os
import shutil
from pathlib import Path

# Folder iz kojeg želimo da premestimo datoteke
source_folder = input("Enter the path to the folder you want to move the files from: ")

# Ciljni folder u koji želimo da premestimo datoteke
destination_folder = input("Enter the path to the target folder: ")

# Tipovi datoteka koje želimo da premestimo
allowed_types = []
print("Enter the types of files you want to move (all, images, video, audio, documents, web, html, python, etc.). When you're done, leave it blank and press Enter.")

while True:
    file_type = input("File type: ").strip().lower()
    if not file_type:
        break
    allowed_types.append(file_type)

# Provera da li su uneti validni putevi foldera
if not os.path.isdir(source_folder) or not os.path.isdir(destination_folder):
    print("Error: One or both of the paths entered are not valid folders.")
    exit()

# Prolazimo kroz sve datoteke u source folderu
for filename in os.listdir(source_folder):
    source_path = os.path.join(source_folder, filename)

    # Proveravamo da li je datoteka i da li je odgovarajućeg tipa
    if os.path.isfile(source_path):
        file_extension = Path(filename).suffix.lower()[1:]
        if 'all' in allowed_types or \
           (file_extension in ['jpg', 'png', 'gif', 'bmp', 'tiff'] and 'images' in allowed_types) or \
           (file_extension in ['mp4', 'avi', 'mkv', 'mov'] and 'video' in allowed_types) or \
           (file_extension in ['mp3', 'wav', 'flac', 'ogg'] and 'audio' in allowed_types) or \
           (file_extension in ['txt', 'doc', 'docx', 'pdf', 'xls', 'xlsx'] and 'documents' in allowed_types) or \
           (file_extension in ['html', 'css', 'js', 'jsx'] and 'web' in allowed_types) or \
           (file_extension == 'html' and 'html' in allowed_types) or \
           (file_extension in ['py', 'pyc', 'pyo'] and 'python' in allowed_types):
            destination_path = os.path.join(destination_folder, filename)
            shutil.move(source_path, destination_path)
            print(f"I moved {filename} to {destination_folder}")

print("Finished!")
input('Please press any key to exit...')
