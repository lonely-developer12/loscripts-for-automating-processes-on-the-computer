import os
import shutil
from pathlib import Path

# Folder iz kojeg želimo da premestimo datoteke
source_folder = input("Enter the path to the folder you want to move the files from: ")

# Ciljni folder u koji želimo da premestimo datoteke
destination_folder = input("Enter the path to the target folder: ")

# Tipovi datoteka koje želimo da premestimo
allowed_types = []
print("Enter the types of files you want to move (images, video, audio, documents). When you're done, leave it blank and press Enter.")

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
        if file_extension in ['jpg', 'png', 'gif', 'bmp', 'tiff'] and 'images' in allowed_types:
            destination_path = os.path.join(destination_folder, filename)
        elif file_extension in ['mp4', 'avi', 'mkv', 'mov'] and 'video' in allowed_types:
            destination_path = os.path.join(destination_folder, filename)
        elif file_extension in ['mp3', 'wav', 'flac', 'ogg'] and 'audio' in allowed_types:
            destination_path = os.path.join(destination_folder, filename)
        elif file_extension in ['txt', 'doc', 'docx', 'pdf', 'xls', 'xlsx'] and 'dokuments' in allowed_types:
            destination_path = os.path.join(destination_folder, filename)
        else:
            continue
        
        # Premestamo datoteku
        shutil.move(source_path, destination_path)
        print(f"I moved it {filename} in {destination_folder}")

print("finish!")
input('please press any key')
