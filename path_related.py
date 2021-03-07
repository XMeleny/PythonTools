import os


def split_url(url):
    (_dir, file) = os.path.split(url)
    temp = file.split('.')
    filename = temp[0]
    ext = temp[1]
    return {'dir': _dir, 'filename': filename, 'ext': ext}


if __name__ == '__main__':
    print(split_url(r"C:\Users\Meleny\Desktop\m'file\compulsory courses\GraduationProject\dataset\video\res_test.mp4"))
