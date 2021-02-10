import xml.etree.ElementTree as ET
import os

classes = ['n', 'p']


def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def convert_file(src_url):
    (file, ext) = os.path.splitext(src_url)
    des_url = file + ".txt"

    in_file = open(src_url)
    out_file = open(des_url, 'w')

    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        cls = obj.find('name').text
        if cls not in classes:
            continue
        cls_id = classes.index(cls)
        xml_box = obj.find('bndbox')
        b = (float(xml_box.find('xmin').text),
             float(xml_box.find('xmax').text),
             float(xml_box.find('ymin').text),
             float(xml_box.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

    in_file.close()
    out_file.close()


def handle_dir(dir_url):
    a = os.walk(dir_url)
    for path, dir_list, file_list in a:
        for file in file_list:
            p = os.path.join(path, file)
            convert_file(p)


if __name__ == '__main__':
    handle_dir(r"C:\Users\Meleny\Desktop\m'file\compulsory courses\GraduationProject\dataset\train_xml")
