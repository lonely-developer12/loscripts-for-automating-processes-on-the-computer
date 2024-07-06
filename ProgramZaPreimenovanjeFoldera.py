import tkinter as tk
from tkinter import filedialog
import os
import shutil

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_label.config(text=folder_path)

def rename_folder():
    new_name = name_entry.get()
    if not new_name:
        return
    
    folder_path = folder_label.cget("text")
    if not folder_path:
        return
    
    folder_dir, old_name = os.path.split(folder_path)
    new_folder_path = os.path.join(folder_dir, new_name)
    try:
        shutil.move(folder_path, new_folder_path)
        folder_label.config(text=new_folder_path)
        root.quit()  # Zatvori program nakon uspešnog preimenovanja
    except Exception as e:
        print(f"Greška pri preimenovanju foldera {old_name}: {e}")

def on_close():
    folder_path = folder_label.cget("text")
    if folder_path:
        root.destroy()  # Zatvori program ako je folder promenjen
    else:
        root.quit()  # Zatvori program ako folder nije promenjen

root = tk.Tk()
root.title("Preimenovanje foldera")
root.protocol("WM_DELETE_WINDOW", on_close)  # Pozovi on_close funkciju kada se prozor zatvori

select_button = tk.Button(root, text="Odaberi folder", command=select_folder)
select_button.pack(pady=10)

folder_label = tk.Label(root, text="")
folder_label.pack(pady=10)

name_label = tk.Label(root, text="Novo ime foldera:")
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack(pady=10)

rename_button = tk.Button(root, text="Preimenuj folder", command=rename_folder)
rename_button.pack(pady=10)

root.mainloop()
