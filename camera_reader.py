# -*- coding:utf-8 -*-

import cv2
from owner_train import Model
from show_image import show_image

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    cascade_path = "/usr/local/opt/opencv/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml"
    model = Model()
    model.load()
    while True:
        _, frame = cap.read()

        # gray conversion
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # get eigenvalues
        cascade = cv2.CascadeClassifier(cascade_path)

        # face detecting
        facerect = cascade.detectMultiScale(frame_gray, scaleFactor=1.2, minNeighbors=3, minSize=(10, 10))
        if len(facerect) > 0:
            print('face detected')
            color = (255, 255, 255)
            for rect in facerect:
                x, y = rect[0:2]
                width, height = rect[2:4]
                image = frame[y - 10: y + height, x: x + width]

                result = model.predict(image)
                if result == 0:  # owner
                    print('Owner detected!')
                    show_image()
                else:            # not owner
                    print('You are not the owner.')

        # waiting key
        k = cv2.waitKey(100)
        # Press Esc to exit...
        if k == 27:
            break

    # Release
    cap.release()
    cv2.destroyAllWindows()
