from rembg import remove
from PIL import Image

input_path = "hamm.jpg"
output_path = "remover.png"
class remove_bg_class:

        def __init__(self, input_path, output_path):
            self.input_path = input_path
            self.output_path = output_path

        def remove_bg(self):
            input_image = Image.open(self.input_path)
            output_image = remove(input_image)
            output_image.save(self.output_path)
            print("success")

remover = remove_bg_class(input_path, output_path)
remover.remove_bg()
