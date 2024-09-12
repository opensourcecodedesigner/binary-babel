import tkinter as tk
from tkinter import filedialog
import numpy as np

class ImageBinaryConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Babel")
        self.binary_data = None
        self.image_data = None

        # Create GUI elements
        self.upload_button = tk.Button(root, text="Upload Image", command=self.upload_image)
        self.upload_button.pack()

        self.binary_text = tk.Text(root, height=5, width=40)
        self.binary_text.pack()

        self.copy_button = tk.Button(root, text="Copy Binary", command=self.copy_binary)
        self.copy_button.pack()

        self.paste_button = tk.Button(root, text="Paste Binary", command=self.paste_binary)
        self.paste_button.pack()

        self.download_button = tk.Button(root, text="Download Image", command=self.download_image)
        self.download_button.pack()

        self.result_text = tk.Text(root, height=5, width=40)
        self.result_text.pack()

    def upload_image(self):
        filepath = filedialog.askopenfilename()
        if filepath:
            self.image_data = open(filepath, "rb").read()
            self.binary_data = self.image_to_binary(self.image_data)
            self.binary_text.insert("1.0", self.binary_data)
            self.result_text.insert("1.0", "Image uploaded successfully!")

    def image_to_binary(self, image_data):
        return image_data.hex()

    def copy_binary(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.binary_text.get("1.0", "end-1c"))

    def paste_binary(self):
        self.binary_data = self.root.clipboard_get()
        self.binary_text.delete("1.0", "end")
        self.binary_text.insert("1.0", self.binary_data)
        self.binary_to_image()

    def binary_to_image(self):
        if self.binary_data:
            self.image_data = bytes.fromhex(self.binary_data)
            self.result_text.insert("1.0", "Binary converted to image successfully!")

    def download_image(self):
        if self.image_data:
            filepath = filedialog.asksaveasfilename(defaultextension=".png")
            if filepath:
                with open(filepath, "wb") as f:
                    f.write(self.image_data)
                self.result_text.insert("1.0", "Image downloaded successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    converter = ImageBinaryConverter(root)
    root.mainloop()