import tkinter as tk
from tkinter import filedialog
import shutil
import os

root = None  # Globalna promenljiva za instancu Tkinter prozora

# Definišemo promenljive izvan funkcija
source_folder_label = None
destination_folder_label = None
file_extensions_entry = None

def select_source_folder():
    source_folder = filedialog.askdirectory(title="Odaberite izvorni folder")
    if source_folder:
        source_folder_label.config(text=source_folder)

def select_destination_folder():
    destination_folder = filedialog.askdirectory(title="Odaberite odredišni folder")
    if destination_folder:
        destination_folder_label.config(text=destination_folder)

def copy_files():
    source_folder = source_folder_label.cget("text")
    destination_folder = destination_folder_label.cget("text")
    file_extensions = file_extensions_entry.get().split(",")

    if not source_folder or not destination_folder or not file_extensions:
        return

    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if any(file.endswith(ext.strip()) for ext in file_extensions):
                source_path = os.path.join(root, file)
                destination_path = os.path.join(destination_folder, file)
                try:
                    shutil.copy2(source_path, destination_path)
                    print(f"Kopirana datoteka: {file}")
                except Exception as e:
                    print(f"Greška pri kopiranju datoteke {file}: {e}")

    root.quit()  # Zatvori program nakon uspešnog kopiranja datoteka

def on_close():
    source_folder = source_folder_label.cget("text")
    destination_folder = destination_folder_label.cget("text")
    if source_folder and destination_folder:
        root.destroy()  # Zatvori program ako su folderi izabrani
    else:
        root.quit()  # Zatvori program ako folderi nisu izabrani

def main():
    global root, source_folder_label, destination_folder_label, file_extensions_entry
    root = tk.Tk()
    root.title("Kopiranje datoteka")
    root.protocol("WM_DELETE_WINDOW", on_close)  # Pozovi on_close funkciju kada se prozor zatvori

    source_folder_label = tk.Label(root, text="Izvorni folder:")
    source_folder_label.pack()

    source_folder_button = tk.Button(root, text="Odaberi izvorni folder", command=select_source_folder)
    source_folder_button.pack()

    destination_folder_label = tk.Label(root, text="Odredišni folder:")
    destination_folder_label.pack()

    destination_folder_button = tk.Button(root, text="Odaberi odredišni folder", command=select_destination_folder)
    destination_folder_button.pack()

    file_extensions_label = tk.Label(root, text="Ekstenzije datoteka (razdvojene zarezom):")
    file_extensions_label.pack()

    file_extensions_entry = tk.Entry(root)
    file_extensions_entry.pack()

    copy_button = tk.Button(root, text="Kopiraj datoteke", command=copy_files)
    copy_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
