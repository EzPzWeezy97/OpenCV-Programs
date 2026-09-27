import cv2
import numpy as np
# print(cv2.__version__)
width=640
height=420
evt = 0 #crash prevention (including x and yval)
Xval=0
Yval=0

def mouseClickFunc(event,xPos,yPos,flag,parameters):
    global evt
    global Xval
    global Yval
    if event == cv2.EVENT_LBUTTONDOWN:
        Xval=xPos
        Yval=yPos
        evt=event
    if event==cv2.EVENT_RBUTTONUP:
        evt=event
        print(event)
camera = cv2.VideoCapture(0) #makes camera object and uses video function with the camera in use as argument (typically 0-4 depending on port camera is plugged into)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, width) #sets camera window width
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height) #sets camera window height
cv2.namedWindow('Camera')
cv2.setMouseCallback('Camera', mouseClickFunc)
while True: #infinite loop to run camera
    ignore, frame = camera.read() #read a fram from camera
    if evt ==1: #if left mouse button down (every mouse click has different value)
        x=np.zeros([250,250,3],dtype=np.uint8) #establishes x basically as all rows and columns of window are black
        color=frame[Yval][Xval]
        print(color)
        x[:,:]=color # all rows and cols of x = its BGR color vals (0-255,0-255,0-255) 
        cv2.putText(x,str(color),(0,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),1)
        evt=0 #resets evt as to not constantly be running
        cv2.imshow('color picker window',x) #shoes color clicked in color window
        cv2.moveWindow('color picker window',width,0)
    cv2.imshow('Camera', frame) #from camera show frame (first argument is just naming the camera window, can be anything)
    if cv2.waitKey(1) == ord('q'):  #waits 1 ms (waitkey arg) and sees if ordinance (value) of q is pressed. If is then breaks out of while loop. note that & 0xff could need to be between waitkey func and == on certain systems such as windows
        break
cam.release() #releases camera