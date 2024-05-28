import tkinter as tk
from src.views.main_view import MainView
from src.models.main_model import MainModel
from src.controllers.main_controller import MainController

class App: 
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("My Visualizer")
        self.root.geometry("800x600")
        self.main_view = MainView(self.root)
        self.main_model = MainModel()
        self.main_controller = MainController(self.main_view, self.main_model)
        
    def run(self):
        self.root.mainloop()