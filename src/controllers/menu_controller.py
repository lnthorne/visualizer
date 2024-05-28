from src.views.audio_view import AudioView
from src.views.image_view import ImageView
from src.controllers.audio_controller import AudioController
from src.controllers.image_controller import ImageController

class MenuController:
    def __init__(self, view):
        self.view = view
        self.view.set_controller(self)

    def show_audio_visualizer(self):
        self.clear_view()
        audio_view = AudioView(self.view.root)
        AudioController(audio_view)

    def show_image_viewer(self):
        self.clear_view()
        image_view = ImageView(self.view.root)
        ImageController(image_view)

    def clear_view(self):
        for widget in self.view.root.winfo_children():
            widget.destroy()