#run: python3 main.py
from pathlib import Path
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def main():
    
    root = tk.Tk()
    root.title("Sort by Extension")
    root.geometry("700x200")

    source_folder_entry = ttk.Entry(root, width=50, state="readonly")
    source_folder_entry.grid(row=0, column=6)
    source_folder_button = ttk.Button(root, text="Add Source Folder", command=add_source_folder)
    source_folder_button.grid(row=0, column=0)

    dest_folder_entry = ttk.Entry(root, width=50, state="readonly")
    dest_folder_entry.grid(row=6, column=6)
    dest_folder_button = ttk.Button(root, text="Add Destination Folder", command=add_dest_folder)
    dest_folder_button.grid(row=6, column=0)

    options = [".png", ".jpg", "docx", ".pdf"]
    dropdown = ttk.Combobox(root, values=options, state="readonly")
    dropdown.grid(row=12, column=0)
    dropdown_entry = ttk.Entry(root, width=20, state="readonly")
    dropdown_entry.grid(row=12, column=6)
    

    root.mainloop()

def add_source_folder():
    folder_path = filedialog.askdirectory(initialdir="/mnt/c/users", title="Select Folder")
    source_folder_entry.insert(str(folder_path))
def add_dest_folder():
    folder_path = filedialog.askdirectory(initialdir="/mnt/c/users", title="Select Folder")

main()