from rembg import remove
from PIL import Image

input_path = "ship.bmp"
output_path = "ship-1.bmp"
input = Image.open(input_path)
output = remove(input)
output.save(output_path)
