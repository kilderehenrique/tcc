from __future__ import print_function 
import cv2
from random import randint
import sys

class VideoFaceDetector:


    def __init__(self, video_path, cascade_path):
        self.face_cascade = cv2.CascadeClassifier(cascade_path)
        self.cap = cv2.VideoCapture(video_path)
       
        success, self.frame = self.cap.read()
        if not success:
            print('Failed to read video')
            sys.exit(1)

    def detect_faces(self):
        bboxes = []
        colors = [] 
        while True:
           bbox = cv2.selectROI('Multitracker', self.frame)
           bboxes.append(bbox)
           colors.append((randint(0, 255), randint(0, 255), randint(0, 255)))
           k = cv2.waitKey(0) & 0xFF
           if (k == 113): 
               break 

        self.cap.release()
        cv2.destroyAllWindows()

        print('Selected bounding boxes {}'.format(bboxes))



# Usage
video_path = '/home/vinicius/visao_computacional/assets/4K Video of Highway Traffic!.mp4'
cascade_path = '/home/vinicius/visao_computacional/data/haarcascades/haarcascade_frontalface_default.xml'
detector = VideoFaceDetector(video_path, cascade_path)
detector.detect_faces()