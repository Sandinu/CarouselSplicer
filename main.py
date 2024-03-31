from tkinter import ttk
import os
import tkinter as tk
from tkinter import filedialog
from tkinterdnd2 import *
from Functionalities import image_slice

def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        output_folder = os.path.dirname(file_path)
        generate_pdf = pdf_checkbox_var.get()
        image_slice(file_path, output_folder, generate_pdf)


def on_drop(event):
    file_path = event.data.strip()
    file_path = file_path.replace("{", "").replace("}", "")
    if file_path:
        output_folder = os.path.dirname(file_path)
        generate_pdf = pdf_checkbox_var.get()
        image_slice(file_path, output_folder, generate_pdf)

if __name__ == "__main__":
    root = TkinterDnD.Tk()
    root.title("Carousel Splicer")
    root.geometry("500x500")
    root.configure(bg='#000')

    style = ttk.Style()
    style.configure('TLabel', font=("Poppins", 13), foreground='white', background='black')
    instruction = ttk.Label(root, text="Select the image or drag and drop an image here")
    instruction.pack(pady=10)

    select_image_btn = tk.Button(root, text="Select Image", command=select_image, font=("Poppins", 12), bg='red', fg='white')
    select_image_btn.pack(pady=10)

    drop_target_frame = tk.Frame(root, width=300, height=300, borderwidth=2, relief="sunken", bg='gray')
    drop_target_frame.pack(pady=10)

    drop_target_frame.drop_target_register(DND_FILES)

    drop_target_frame.dnd_bind('<<Drop>>', on_drop)

    pdf_checkbox_var = tk.BooleanVar()
    pdf_checkbox = tk.Checkbutton(root, text="Generate PDF", variable=pdf_checkbox_var, font=("Poppins", 12), bg='#000', fg='white', selectcolor='#000')
    pdf_checkbox.pack(pady=5)

    root.mainloop()

