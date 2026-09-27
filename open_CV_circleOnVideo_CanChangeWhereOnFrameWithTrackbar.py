import cv2
# print(cv2.__version__)
width=1280
height=720
xPos = int(width/2) #xPos,yPos,and myRad variables here are just to have them established so program doesn't crash but do change as program runs
yPos= int(height/2)
myRad = 25

def myXCallbackFunction(value):
    global xPos
    print('xPos: ', value)
    xPos = value

def myYCallbackFunction(value):
    global yPos
    print('yPos: ', value)
    yPos = value

def myRadCallbackFunction(value):
    global myRad
    print('Radius: ', value)
    myRad = value

camera = cv2.VideoCapture(0) #makes camera object and uses video function with the camera in use as argument (typically 0-4 depending on port camera is plugged into)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, width) #sets camera window width
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height) #sets camera window height
cv2.namedWindow('myTrackbars') #creates window named myTrackbars for trackbar 
cv2.resizeWindow('myTrackbars',400,350) #resizes trackbar window
cv2.moveWindow('myTrackbars',width,0) #moves trackbar window as to not be behind or in front of main window
cv2.createTrackbar('xPos','myTrackbars',0,1920,myXCallbackFunction) #creates xpos trackbar, args: name of trackbar, name of window used,beginning of where trackbar starts from whe opened (lower limit always zero and cant be changed) , end of where trackbar measures (can be changed and is upper limit) , callback function for actions during events
cv2.createTrackbar('yPos','myTrackbars',540,1080,myYCallbackFunction) #creates yPos track bar
cv2.createTrackbar('radius','myTrackbars',myRad,int(height/2),myRadCallbackFunction)
while True: #infinite loop to run camera
    ignore, frame = camera.read() #read a fram from camera
    cv2.circle(frame,(xPos,yPos),myRad,(255,0,0),2) #creates circle on screen (this one controlled by trackbar)
    cv2.imshow('Camera', frame) #from camera show frame (first argument is just naming the camera window, can be anything)
    if cv2.waitKey(1) == ord('q'):  #waits 1 ms (waitkey arg) and sees if ordinance (value) of q is pressed. If is then breaks out of while loop. note that & 0xff could need to be between waitkey func and == on certain systems such as windows
        break
cam.release() #releases camera
