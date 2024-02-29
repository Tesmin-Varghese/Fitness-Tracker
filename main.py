import poseModule as pm
import cv2
import numpy as np

detector= pm.poseDetector()

video_capture = cv2.VideoCapture('/home/tesmin/Downloads/vscode/Fitness tracker/squat.mp4')

count=0
direction = 0  #to find if the person is standing or crouching

while True:
    success,img=video_capture.read()
    img= cv2.resize(img,(1280,720))

    img=detector.findPose(img,draw=False)
    lmlist = detector.findPosition(img,draw=False)
    #print(lmlist)

    if len(lmlist)!=0:
        angle = detector.findAngle(img,24,26,28)  #here we count squats , so we need to find the angles of knees, so we take 24,26,28 for right knee
        low_angle = 35
        high_angle=170

        percentage = np.interp(angle,(low_angle,high_angle),(0,100))  #convert all angle values convert to 0(low values) or 100(high values) or between 0 and 100

        #print(angle,'===>',percentage)  # executing this line will give better understanding about conversion using interpolation in numpy

        if percentage ==100:  #standing position
           if direction == 0:  #person is going to crouch/going down
              count+=0.5
              direction = 1   #direction changed to one, when the person stand
        if percentage==0:  #sitting position
           if direction == 1:  #going to stand/moving towards up
              count+=0.5
              direction=0 #direction changed to 0, person is sitting

        print(int(count))


    cv2.imshow('video_capture',img)

    if cv2.waitKey(1) & 0xFF==27:
      break
  
video_capture.release()
cv2.destroyAllWindows()