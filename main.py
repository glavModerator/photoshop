from PIL import Image
from PIL import ImageFilter

with Image.open("niger.jpg") as image_original:
    image_original.show()

    image_gray = image_original.convert("L")
    image_gray.save("niger_grey.jpg")
    image_gray.show()

    image_blur = image_original.filter(ImageFilter.BLUR)
    image_blur.save("niger_blur.jpg")

    image_rotate = image_original.transpose(Image.ROTATE_180)
    image_rotate.save("niger_rotate.jpg")