import cv2
import os

video_path = r"C:\Users\Meleny\Documents\Tencent Files\865622793\FileRecv\video.mp4"
save_dir_path = r"C:\Users\Meleny\Documents\Tencent Files\865622793\FileRecv\frames"

video_capture = cv2.VideoCapture(video_path)

count = 2
i = 0
j = 0

while True:
    success, frame = video_capture.read()
    if success:
        if i % count == 0:
            j += 1
            save_name = "frame" + str(j) + ".jpg"
            cv2.imwrite(os.path.join(save_dir_path, save_name), frame)
    else:
        break
    i += 1

video_capture.release()
