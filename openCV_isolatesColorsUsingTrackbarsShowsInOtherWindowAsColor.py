import cv2
import numpy as np
# print(cv2.__version__)
width=640
height=420
hueLow=0 #initializing these as to not crash program
hueHigh=0
satLow=0
satHigh=0
valLow=0
valHigh=0

#all relative trackbar functions below

def onTrack1(val):
    global hueLow
    hueLow=val
    print('Hue Low ', hueLow)

def onTrack2(val):
    global hueHigh
    hueHigh=val
    print('Hue High ', hueHigh)

def onTrack3(val):
    global satLow
    satLow=val
    print('Saturation Low ', satLow)

def onTrack4(val):
    global satHigh
    satHigh=val
    print('Saturation High ', satHigh)

def onTrack5(val):
    global valLow
    valLow=val
    print('Value Low ', valLow)

def onTrack6(val):
    global valHigh
    valHigh=val
    print('Value High ', valHigh)

camera = cv2.VideoCapture(0) #makes camera object and uses video function with the camera in use as argument (typically 0-4 depending on port camera is plugged into)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, width) #sets camera window width
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height) #sets camera window height

#this block of code is all the trackbars setup
cv2.namedWindow('myTrackbars')
cv2.moveWindow('myTrackbars',width+50,0)
cv2.createTrackbar('Hue Low', 'myTrackbars',0,179, onTrack1)
cv2.createTrackbar('Hue High', 'myTrackbars',0,179, onTrack2)
cv2.createTrackbar('Saturation Low', 'myTrackbars',0,255, onTrack3)
cv2.createTrackbar('Saturation High', 'myTrackbars',0,255, onTrack4)
cv2.createTrackbar('Value Low', 'myTrackbars',0,255, onTrack5)
cv2.createTrackbar('Value High', 'myTrackbars',0,255, onTrack6)


while True: #infinite loop to run camera
    ignore, frame = camera.read() #read a fram from camera
    frameHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #makes frame for HSV colors to isolate 
    lowerBound=np.array([hueLow,satLow,valLow]) #variable for lowerbounds 0f H,S, and V
    upperBound=np.array([hueHigh,satHigh,valHigh])# variable for upperbounds of H,S, and V
    myMask=cv2.inRange(frameHSV,lowerBound,upperBound) #makes a mask that showes pixels (in black and white) shown only by HSV value in our set within lower and upperbound range
    myObject=cv2.bitwise_and(frame, frame, mask=myMask)
    cv2.imshow('My Object', myObject)
    #cv2.imshow('myMask', myMask) #shows mask window
    myMaskSmall=cv2.resize(myMask,(int(width/2),int(height/2))) #smaller mask window
    cv2.imshow('myMaskSmall',myMaskSmall)
    cv2.moveWindow('myMaskSmall',0,height+50)
    cv2.imshow('Camera', frame) #from camera show frame (first argument is just naming the camera window, can be anything)
    if cv2.waitKey(1) == ord('q'):  #waits 1 ms (waitkey arg) and sees if ordinance (value) of q is pressed. If is then breaks out of while loop. note that & 0xff could need to be between waitkey func and == on certain systems such as windows
        break
cam.release() #releases camera

















































































































































































































































































































































