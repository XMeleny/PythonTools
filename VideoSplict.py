import cv2
import os
import path_related


def get_save_info(video_url):
    split_result = path_related.split_url(video_url)
    save_dir = os.path.join(split_result.get("dir"), split_result.get("filename"))
    save_filename_format = split_result.get("filename") + "_{}.jpg"
    return save_dir, save_filename_format


def split_video(video_url, denominator):
    save_dir, save_filename_format = get_save_info(video_url)

    # create dir for saving
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)

    i = 0
    j = 0
    video_capture = cv2.VideoCapture(video_url)
    while True:
        success, frame = video_capture.read()
        if success:
            if i % denominator == 0:
                j += 1
                save_filename = save_filename_format.format(j)
                save_url = os.path.join(save_dir, save_filename)
                # print(save_url)
                cv2.imwrite(save_url, frame)
        else:
            break
        i += 1

    video_capture.release()


if __name__ == '__main__':
    video_path = r"C:\Users\Meleny\Desktop\m'file\compulsory courses\GraduationProject\dataset\video\res_test.mp4"

    split_video(video_path, 1)
