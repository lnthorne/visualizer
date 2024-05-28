import tkinter as tk
from tkinter import ttk

class MenuView:
    def __init__(self, root):
        self.root = root
        self.frame = ttk.Frame(root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid rows and columns to center content
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_rowconfigure(1, weight=1)
        self.frame.grid_rowconfigure(2, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        self.audio_button = ttk.Button(self.frame, text="Audio Visualizer", command=self.open_audio)
        self.audio_button.grid(row=0, column=0, pady=10)

        self.image_button = ttk.Button(self.frame, text="Image Viewer", command=self.open_image)
        self.image_button.grid(row=1, column=0, pady=10)

        self.exit_button = ttk.Button(self.frame, text="Exit", command=self.exit_app)
        self.exit_button.grid(row=2, column=0, pady=10)

    def set_controller(self, controller):
        self.controller = controller

    def open_audio(self):
        self.controller.show_audio_visualizer()

    def open_image(self):
        self.controller.show_image_viewer()

    def exit_app(self):
        self.root.quit()