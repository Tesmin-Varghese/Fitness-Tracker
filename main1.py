import poseModule as pm
import cv2
import numpy as np 

#import pafy as pf  #use this to directly give youtube link instead of downloading video

detector = pm.poseDetector()

#video_url = "https://www.youtube.com/watch?v=av7-8igSXTs"   #code for pafy
#video = pf.new(video_url)

video=cv2.VideoCapture('/home/tesmin/Downloads/vscode/Fitness tracker/videoplayback.mp4')

count=0
direction=0

while True:
    success,img=video.read()
    img=cv2.resize(img,(1280,720))

    img=detector.findPose(img)
    lmlist=detector.findPosition(img)
    #print(lmlist)

    
    if len(lmlist)!=0:
       angle=detector.findAngle(img,12,14,16)
       #low_angle = 
       #high_angle = 

       #percentage = np.interp(angle,(low_angle,high_angle),(0,100))

       print(angle)


    cv2.imshow('video_capture',img)
    if cv2.waitKey(1) & 0XFF==27:
       break

video.release()
cv2.destroyAllWindows

