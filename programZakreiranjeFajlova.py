import os

def create_files():
    # Dohvati putanju od korisnika
    folder_path = input("Enter the path of the folder where you want to create the files: ")

    # Provjeri postoji li folder
    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' there is not.")
        return

    # Dohvati broj datoteka od korisnika
    num_files = int(input("Enter the number of files you want to create: "))

    # Kreiraj datoteke
    for i in range(num_files):
        filename = input(f"Enter a file name {i+1} : ")
        file_ext = input(f"Enter the extension for the file '{filename}' : ")
        file_path = os.path.join(folder_path, f"{filename}.{file_ext}")

        try:
            with open(file_path, "w") as f:
                pass
            print(f"File '{filename}.{file_ext}' was created in '{folder_path}'.")
        except Exception as e:
            print(f"Error creating file'{filename}.{file_ext}': {e}")

if __name__ == "__main__":
    create_files()
