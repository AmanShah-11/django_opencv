import time
import boto3
import random
import string
import cv2
import numpy as np
import pyautogui
from os import listdir
from os.path import isfile, join

from . import aws_api


class BeginnerVideoFacialDetection:

    # This method is written in a way such that only one face can be detected at a time
    def screenshot_video_camera(self, faces):
        source_files = [f for f in listdir('images/source/')]
        print(source_files)
        target_file = ""
        new_source_file = ""
        for source_file in source_files:
            print(source_file)
            if pyautogui.locateOnScreen("images/source/{}".format(source_file), confidence=0.3):
                for x, y, w, h in faces:
                    my_screenshot = pyautogui.screenshot(region=[x, y, x+w, y+h])
                    # my_screenshot = pyautogui.hotkey('alt', 'printscreen')
                    my_screenshot = cv2.cvtColor(np.array(my_screenshot), cv2.COLOR_RGB2BGR)
                    target_file = "".join(random.choice(string.ascii_lowercase) for i in range(10)) + ".png"
                    print(target_file)
                    cv2.imwrite("images/target/{}".format(target_file), my_screenshot)
                    new_source_file = source_file
                    break
            else:
                print("No match???????")
        return new_source_file, target_file

    def load_video_camera(self):
        # casc_path = sys.argv[0]
        source_file, target_file = "", ""
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

        video_capture = cv2.VideoCapture(0)
        count = 0
        while True:
            # Capture frame-by-frame
            ret, frame = video_capture.read()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # current = time.time()
            # delta =+ current - previous
            # previous = current

            faces = face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                # flags=cv2.cv.CV_HAAR_SCALE_IMAGE
            )

            # Draw a rectangle around the faces
            for (x, y, w, h) in faces:
                 cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

            # Display the resulting frame
            cv2.imshow('Video', frame)
            # print(count)
            # print(delta)
            # time.sleep(10)
            # source_file, target_file = self.screenshot_video_camera2(faces)
            # if (source_file != ""):
            #     break
            if count > 25:
                source_file, target_file = self.screenshot_video_camera(faces)
                break
            count = count + 1
            # if cv2.waitKey(1) & 0xFF == ord('s'):
            #
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # When everything is done, release the capture
        video_capture.release()
        cv2.destroyAllWindows()
        return source_file, target_file