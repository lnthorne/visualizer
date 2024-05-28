import tkinter as tk
from tkinter import ttk, filedialog

class MainView: 
    def __init__(self, root):
        self.root = root
        self.frame = ttk.Frame(self.root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.canvas = tk.Canvas(self.frame, width=600, height=400, bg="white")
        self.canvas.grid(row=0, column=0, columnspan=2, pady=20)

        self.open_button = ttk.Button(self.frame, text="Open .wav File", command=self.open_file)
        self.open_button.grid(row=1, column=0, pady=10)

        self.info_label = ttk.Label(self.frame, text="No file loaded")
        self.info_label.grid(row=1, column=1, pady=10)


    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("WAV files", "*.wav")])
        if file_path:
            self.controller.load_file(file_path)

    def set_controller(self, controller):
        self.controller = controller


    def display_waveform(self, left_channel, right_channel):
        self.canvas.delete("all")
        width = int(self.canvas["width"])
        height = int(self.canvas["height"])
        mid = height // 2

        # Left channel
        prev_x = 0
        prev_y = mid
        for i in range(len(left_channel)):
            x = int(i * width / len(left_channel))
            y = int(mid - (left_channel[i] * mid))
            self.canvas.create_line(prev_x, prev_y, x, y, fill="blue")
            prev_x = x
            prev_y = y
        
        #Right channel
        prev_x = 0
        prev_y = mid
        for i in range(len(right_channel)):
            x = int(i * width / len(right_channel))
            y = int(mid - (right_channel[i] * mid))
            self.canvas.create_line(prev_x, prev_y, x, y, fill="red")
            prev_x = x
            prev_y = y

    def display_info(self, num_samples, sample_rate):
        self.info_label.config(text=f"Samples: {num_samples}, Sample Rate: {sample_rate}")