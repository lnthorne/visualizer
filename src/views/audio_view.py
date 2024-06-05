import tkinter as tk
from tkinter import ttk, filedialog

class AudioView: 
    def __init__(self, root):
        self.root = root
        self.frame = ttk.Frame(self.root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        self.canvas = tk.Canvas(self.frame, width=600, height=400, bg="white")
        self.canvas.grid(row=0, column=0, columnspan=2, pady=20)

        self.button_frame = ttk.Frame(self.frame, padding="10")
        self.button_frame.grid(row=1, column=0, pady=10, sticky=(tk.W, tk.E))

        self.open_button = ttk.Button(self.button_frame, text="Open .wav File", command=self.open_file)
        self.open_button.grid(row=0, column=0, padx=5)

        self.exit_button = ttk.Button(self.button_frame, text="Exit", command=self.exit_app)
        self.exit_button.grid(row=0, column=1, padx=5)

        self.info_label = ttk.Label(self.frame, text="No file loaded")
        self.info_label.grid(row=1, column=1, pady=10, padx=(0, 100))


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
        mid_left = height // 4
        mid_right = 3 * height // 4
        y_scale = height // 4

        # Plot left channel
        prev_x = 0
        prev_y = mid_left
        x_step_size = width / len(left_channel)
        for i in range(len(left_channel)):
            x = int(i * x_step_size)
            y = int(mid_left - (left_channel[i] * y_scale))
            self.canvas.create_line(prev_x, prev_y, x, y, fill="blue")
            prev_x = x
            prev_y = y

        # Plot right channel
        prev_x = 0
        prev_y = mid_right
        x_step_size = width / len(right_channel)
        for i in range(len(right_channel)):
            x = int(i * x_step_size)
            y = int(mid_right - (right_channel[i] * y_scale))
            self.canvas.create_line(prev_x, prev_y, x, y, fill="red")
            prev_x = x
            prev_y = y

    def display_info(self, num_samples, sample_rate):
        self.info_label.config(text=f"Samples: {num_samples}, Sample Rate: {sample_rate}")
    
    def exit_app(self):
        self.root.quit()