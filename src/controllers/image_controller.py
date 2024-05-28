from PIL import Image

class ImageController:
    def __init__(self, view):
        self.view = view
        self.view.set_controller(self)

    def load_image(self, image_path):
        image = Image.open(image_path)
        self.view.display_image(image)