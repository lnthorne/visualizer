import tkinter as tk
from src.views.menu_view import MenuView
from src.controllers.menu_controller import MenuController

class App: 
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("My Visualizer")
        self.root.geometry("800x600")
        self.main_view = MenuView(self.root)
        self.main_controller = MenuController(self.main_view)
        
    def run(self):
        self.root.mainloop()