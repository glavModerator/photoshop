from PIL import Image


class ImageEditer:
    def  __init__(self, filename):
        self.filename = filename
        self.original = None
        self.changer = []


    def open(self):
        try:
            self.original = Image.open(self.filename)
            self.original.show()
        except:
            print('Файл не знайдено! ')


    def do_left(self):
        rotated = self.original.transport(Image.FLIP_LEFT_RIGHT)
        self.changed.append(rotated)


        temp_filename = self.filename.split('.')
        new_filename = temp_filename[0] + str(len(self.changed)) + temp_filename[-1]