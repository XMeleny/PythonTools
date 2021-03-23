import cv2
import numpy as np
import path_related

import skvideo
import skvideo.io

skvideo.setFFmpegPath(r"C:\Users\Meleny\ffmpeg-4.3.2-2021-02-02-full_build\bin")


# 得到旋转角度之后，对视频帧旋转对应的负角度便可以得到正向的图像
def rotate_img_data(img_data, degree):
    h, w = img_data.shape[:2]
    (cx, cy) = (w / 2, h / 2)

    # 设置旋转矩阵
    M = cv2.getRotationMatrix2D((cx, cy), -degree, scale=1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])

    # 计算图像旋转后的新边界
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))

    # 调整旋转矩阵的移动距离（t_{x}, t_{y}）
    M[0, 2] += (nW / 2) - cx
    M[1, 2] += (nH / 2) - cy

    img_rotated = cv2.warpAffine(img_data, M, (nW, nH))
    return img_rotated


def get_rotate_degree(video_path):
    video_metadata = skvideo.io.ffprobe(video_path)
    degree = 0
    for tag_info in video_metadata['video']['tag']:
        for key, val in tag_info.items():
            if val == "rotate":
                degree = int(tag_info["@value"])  # 原来是float
                break
        break
    # print("degree = {}".format(degree))
    return degree


def rotate_video(video_path, degree):
    if degree % 360 != 0 and degree % 90 == 0:
        # 获取source的相关属性
        src_video = cv2.VideoCapture(src_filename)
        fourcc = int(src_video.get(cv2.CAP_PROP_FOURCC))
        fps = src_video.get(cv2.CAP_PROP_FPS)
        w = int(src_video.get(cv2.CAP_PROP_FRAME_WIDTH))
        h = int(src_video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        if degree % 180 == 0:
            size = (w, h)
        else:
            size = (h, w)
        print(f"fourcc = {fourcc}, fps = {fps}, size = {size}")

        des_filename = path_related.get_des_file(video_path, suffix=f'rotated{degree}')
        print(f'des_filename = {des_filename}')

        video_writer = cv2.VideoWriter(des_filename, fourcc, fps, size)

        read_status, video_frame = src_video.read()
        while read_status:
            video_frame = rotate_img_data(video_frame.copy(), degree)
            video_writer.write(video_frame)
            read_status, video_frame = src_video.read()

        src_video.release()
        video_writer.release()


if __name__ == "__main__":
    src_filename = r"C:\Users\Meleny\Desktop\m'file\compulsory courses\GraduationProject\dataset\video\test.mp4"
    print(get_rotate_degree(src_filename))
    rotate_video(src_filename, get_rotate_degree(src_filename))
