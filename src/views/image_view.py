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
        self.frame.grid_columnconfigure(0, weight=1)

        self.canvas = tk.Canvas(self.frame, bg="white")
        self.canvas.grid(row=0, column=0, pady=20, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.button_frame = ttk.Frame(self.frame, padding="10")
        self.button_frame.grid(row=1, column=0, pady=10, sticky=(tk.W, tk.E))

        self.open_button = ttk.Button(self.button_frame, text="Open .tif File", command=self.open_file)
        self.open_button.grid(row=0, column=0, padx=5)

        self.exit_button = ttk.Button(self.button_frame, text="Exit", command=self.exit_app)
        self.exit_button.grid(row=0, column=1, padx=5)

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
        self.canvas.config(width=image.width, height=image.height)
        
        self.root.geometry(f"{image.width + 20}x{image.height + 100}")
        self.root.minsize(image.width + 20, image.height + 100)

    def exit_app(self):
        self.root.quit()
