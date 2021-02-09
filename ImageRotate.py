import os
from PIL import Image

dir_path = r"C:\Users\Meleny\Desktop\m'file\compulsory courses\GraduationProject\dataset\test"


def rotate_file(image_path):
    im = Image.open(image_path)
    out = im.transpose(Image.ROTATE_270)
    out.save(image_path)
    pass


for i in os.walk(dir_path):
    for j in i[2]:
        file_path = os.path.join(i[0], j)
        rotate_file(file_path)
