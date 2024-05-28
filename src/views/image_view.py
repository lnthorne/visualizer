import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk

class ImageView:
    def __init__(self, root):
        self.root = root
        self.frame = ttk.Frame(root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_rowconfigure(1, weight=1)
        self.frame.grid_rowconfigure(2, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        self.canvas = tk.Canvas(self.frame, width=600, height=400,  bg="white")
        self.canvas.grid(row=0, column=0, pady=20, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.open_button = ttk.Button(self.frame, text="Open .tif File", command=self.open_file)
        self.open_button.grid(row=1, column=0, pady=10)

        self.exit_button = ttk.Button(self.frame, text="Exit", command=self.root.quit)
        self.exit_button.grid(row=2, column=0, pady=10)

    def set_controller(self, controller):
        self.controller = controller

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("TIFF files", "*.tif")])
        if file_path:
            self.controller.load_image(file_path)

    def display_image(self, image):
        self.canvas.delete("all")
        self.image_tk = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image_tk)
        self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))
