from PIL import Image
a = [256, 256, 0, 256, 256, 256, 256, 256, 0, 256, 256, 256, 256, 256, 0, 256, 256, 256, 256, 256, 0, 256, 256, 256]
img = Image.new("L", (5, 5))
img.putdata(a)
img.save("Advent_of_Code_14_images/image.jpg")