import cv2
# print(cv2.__version__)
width=640
height=420

def myCallbackFunction(value):
    print(value)
    
camera = cv2.VideoCapture(0) #makes camera object and uses video function with the camera in use as argument (typically 0-4 depending on port camera is plugged into)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, width) #sets camera window width
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height) #sets camera window height
cv2.namedWindow('myTrackbars') #creates window named myTrackbars for trackbar 
cv2.resizeWindow('myTrackbars',400,100) #resizes trackbar window
cv2.moveWindow('myTrackbars',width,0) #moves trackbar window as to not be behind or in front of main window
cv2.createTrackbar('xPos','myTrackbars',0,1920,myCallbackFunction) #creates trackbar, args: name of trackbar, name of window used,beginning of where trackbar measures , end of where trackbar measures , callback function for actions during events
while True: #infinite loop to run camera
    ignore, frame = camera.read() #read a fram from camera
    cv2.imshow('Camera', frame) #from camera show frame (first argument is just naming the camera window, can be anything)
    if cv2.waitKey(1) == ord('q'):  #waits 1 ms (waitkey arg) and sees if ordinance (value) of q is pressed. If is then breaks out of while loop. note that & 0xff could need to be between waitkey func and == on certain systems such as windows
        break
cam.release() #releases camera
