import cv2 as cv 
import numpy as np 

cam=cv.VideoCapture(0)

while True:
    ret,frame=cam.read()

    hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    lower_blue=np.array([110,50,50])
    upper_blue=np.array([130,255,255])

    mask=cv.inRange(hsv,lower_blue,upper_blue)
    res=cv.bitwise_and(frame,frame,mask=mask)

    cv.imshow('orignal',frame)
    #cv.imshow('mask',mask)
    cv.imshow('res',res)

    k=cv.waitKey(1)
    if k==27:
    	break

cam.release()
cv.destroyAllWindows()