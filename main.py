#run: python3 main.py
from pathlib import Path
import tkinter as tk
from tkinter import filedialog

def main():
    
    root = tk.Tk()
    root.title("Sort by Extension")
    root.geometry("500x300")

    source_folder_label = tk.Label(root, text="Source Folder")
    source_folder_label.grid(row=0, column=0)
    source_folder_button = tk.Button(root, text="Add Folder", command=add_folder)
    source_folder_button.grid(row=0, column=2)

    dest_folder_label = tk.Label(root, text="Destination Folder")
    dest_folder_label.grid(row=1, column=0)
    dest_folder_button = tk.Button(root, text="Add Folder", command=add_folder)
    dest_folder_button.grid(row=1, column=2)

    root.mainloop()

def add_folder():
    folder_path = filedialog.askdirectory(initialdir="/mnt/c/users", title="Select Folder")
    

main()