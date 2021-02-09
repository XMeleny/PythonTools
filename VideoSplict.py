import cv2
import os

video_path = r"C:\Users\Meleny\Desktop\m'file\compulsory courses\GraduationProject\dataset\test.mp4"
save_dir_path = r"C:\Users\Meleny\Desktop\m'file\compulsory courses\GraduationProject\dataset\test"

video_capture = cv2.VideoCapture(video_path)

count = 1
i = 0
j = 0

while True:
    success, frame = video_capture.read()
    if success:
        if i % count == 0:
            j += 1
            save_name = "test" + str(j) + ".jpg"
            cv2.imwrite(os.path.join(save_dir_path, save_name), frame)
    else:
        break
    i += 1

video_capture.release()

