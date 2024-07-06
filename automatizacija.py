import os
import shutil

# Putanje do izvornog i odredišnog direktorija
source_dir = "c:/Users/hacker/Desktop/test"
dest_dir = "c:/Users/hacker/Desktop/newtest"
print('Running...')
# Iteriramo kroz sve datoteke u izvornom direktoriju
file_count = 1
for filename in os.listdir(source_dir):
    # Konstruiramo potpune putanje do izvorne datoteke
    source_path = os.path.join(source_dir, filename)

    # Generiramo novo ime za odredišnu datoteku
    new_filename = f"test_{file_count}{os.path.splitext(filename)[1]}"
    dest_path = os.path.join(dest_dir, new_filename)

    # Premještamo datoteku iz izvorne u odredišnu putanju
    shutil.move(source_path, dest_path)

    file_count += 1

print("all files have been moved successfully")
input('please press enter :')