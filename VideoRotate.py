import cv2
import skvideo

skvideo.setFFmpegPath(r"C:\Users\Meleny\ffmpeg-4.3.2-2021-02-02-full_build\bin")
import skvideo.io
import numpy as np

import os


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


if __name__ == "__main__":
    src_filename = r"C:\Users\Meleny\Desktop\m'file\compulsory courses\GraduationProject\dataset\video\test.mp4"
    path, filename = os.path.split(src_filename)
    des_filename = os.path.join(path, "res_" + filename)

    # 计算旋转角度
    video_metadata = skvideo.io.ffprobe(src_filename)
    rotate_degree_info = 0
    for tag_info in video_metadata['video']['tag']:
        for key, val in tag_info.items():
            if val == "rotate":
                rotate_degree_info = int(tag_info["@value"])  # 原来是float
        print("Info: video rotate degree info:{}".format(rotate_degree_info))
        break

    # 只有旋转了90度的倍数才继续
    if rotate_degree_info != 0 and rotate_degree_info % 90 == 0:
        # 获取source的相关属性
        src_video = cv2.VideoCapture(src_filename)
        fourcc = int(src_video.get(cv2.CAP_PROP_FOURCC))
        fps = src_video.get(cv2.CAP_PROP_FPS)
        w = int(src_video.get(cv2.CAP_PROP_FRAME_WIDTH))
        h = int(src_video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        if rotate_degree_info % 180 == 0:
            size = (w, h)
        else:
            size = (h, w)
        print(f"fourcc = {fourcc}, fps = {fps}, size = {size}")

        video_writer = cv2.VideoWriter(des_filename, fourcc, fps, size)

        read_status, video_frame = src_video.read()
        while read_status:
            video_frame = rotate_img_data(video_frame.copy(), rotate_degree_info)
            video_writer.write(video_frame)
            read_status, video_frame = src_video.read()

        src_video.release()
        video_writer.release()
