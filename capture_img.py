import os
import time
import uuid
import cv2

IMAGES_PATH = 'Tensorflow/workspace/images/collectedimages'

labels = ['smoking']

number_imgs = 20

for label in labels:
    os.makedirs(f'Tensorflow/workspace/images/collectedimages/{label}', exist_ok=True)
    cap = cv2.VideoCapture(0)
    print('collecting images for {}'.format(label))
    time.sleep(5)
    for imgnum in range(number_imgs):
        ret, frame = cap.read()
        imagename = os.path.join(IMAGES_PATH, label, label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imagename, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()