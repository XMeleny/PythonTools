import os


def split_url(url):
    (_dir, file) = os.path.split(url)
    temp = file.split('.')
    filename = temp[0]
    ext = temp[1]
    return {'dir': _dir, 'filename': filename, 'ext': ext}


def get_des_dir(src_url):
    split_result = split_url(src_url)
    des_dir = os.path.join(split_result['dir'], split_result['filename'])
    # os.mkdir(des_dir)
    return des_dir


def get_des_file(src_url, prefix='', suffix='', ext=''):
    split_result = split_url(src_url)

    # 添加前后缀
    filename = split_result['filename']
    if len(prefix) > 0:
        filename = prefix + "_" + filename
    if len(suffix) > 0:
        filename = filename + "_" + suffix

    # 添加文件格式
    if len(ext) == 0:
        filename = filename + "." + split_result['ext']
    else:
        filename = filename + "." + ext

    des_url = os.path.join(split_result['dir'], filename)
    # print(f'des_url = {des_url}')
    return des_url


if __name__ == '__main__':
    url = r"C:\Users\Meleny\Documents\WeChat Files\wxid_85r3h8z4e22i22\FileStorage\File\2021-01\hyf\promise.js"
    print(get_des_dir(url))
