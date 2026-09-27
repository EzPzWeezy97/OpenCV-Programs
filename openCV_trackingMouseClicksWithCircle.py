import cv2
# print(cv2.__version__)
width=640
height=420
evt = 0 #gives evt a value so doesn't crash
def mouseClick(event,xPos,yPos,flags, parameters): #mouseClick function inside our SetMouseCallback func, 
    global evt #establishes these as global so they arent trapped in if statement
    global point
    if event == cv2.EVENT_LBUTTONDOWN: #leftmouse click down
        print('Mouse event was: ' , event) #specific actions or events are designated by a number i.e. this one = 1 (see below for evt)
        print('at position ', xPos,yPos)
        point = (xPos,yPos)
        evt = event #assists in making this global
    if event == cv2.EVENT_LBUTTONUP: #left mouseclick up (release). designated value = 4
        print('Mouse event was: ' , event)
        print('at position ', xPos,yPos)
        point = (xPos,yPos)
        evt = event
    if event == cv2.EVENT_RBUTTONUP: #right mouseclick up (release). designated value = 5
        print('Mouse event was: ' , event)
        print('at position ', xPos,yPos)
        point = (xPos,yPos)
        evt = event
    if event == cv2.EVENT_RBUTTONDOWN: #right mouse click down. designated value = 2
        print('Mouse event was: ' , event) 
        print('at position ', xPos,yPos)
        point = (xPos,yPos)
        evt = event #assists in making this global
camera = cv2.VideoCapture(0) #makes camera object and uses video function with the camera in use as argument (typically 0-4 depending on port camera is plugged into)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, width) #sets camera window width
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height) #sets camera window height
cv2.namedWindow('Camera')
cv2.setMouseCallback('Camera',mouseClick) #needs to know window to read from(camera) and a function(mouseClick) to desctibe in case of event
while True: #infinite loop to run camera
    ignore, frame = camera.read() #read a fram from camera
    if evt == 1: # if event = left mose click down
        cv2.circle(frame,point,25,(255,0,0),2) 
    cv2.imshow('Camera', frame) #from camera show frame (first argument is just naming the camera window, can be anything)
    if cv2.waitKey(1) == ord('q'):  #waits 1 ms (waitkey arg) and sees if ordinance (value) of q is pressed. If is then breaks out of while loop. note that & 0xff could need to be between waitkey func and == on certain systems such as windows
        break
cam.release() #releases camera