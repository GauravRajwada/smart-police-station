

import cv2
from datetime import datetime
import numpy as np


faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')

def face_extractor(img):
    faces = faceCascade.detectMultiScale(img, 1.3, 5)
    if faces is ():
        return None

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
        cropped_face = img[y:y + h, x:x + w]

    return cropped_face

def capture():
    cap = cv2.VideoCapture(0)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1000)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1400)
    cv2.moveWindow('image', 200, 200)

    t=150
    while t:
        t-=1

        _, frame = cap.read()
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        face = face_extractor(frame)
        if type(face) is np.ndarray:


            cv2.putText(frame,"Press Q to capture   Countdown:"+str(t), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(frame, str(time), (900, 50), cv2.FONT_HERSHEY_COMPLEX, 1,(0, 255, 0), 2)
            key = cv2.waitKey(1)
            if key == ord('q'):
                showPic = cv2.imwrite("victim.jpg", frame)
                cap.release()
                cv2.destroyAllWindows()
                return showPic

                break
        else:
            cv2.putText(frame, "No face found      Countdown:"+str(t), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(frame, str(time), (900, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('Video', frame)
        cv2.waitKey(1)

    cap.release()
    cv2.destroyAllWindows()
