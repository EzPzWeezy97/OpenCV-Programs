import cv2
# print(cv2.__version__)
width=640
height=420
camera = cv2.VideoCapture(0) #makes camera object and uses video function with the camera in use as argument (typically 0-4 depending on port camera is plugged into)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, width) #sets camera window width
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height) #sets camera window height

#line below creates object to pull from trained facial DETECTION model to be used in our while loop reading frames. the argument is just the path to the model we want to use
faceCascadeObject = cv2.CascadeClassifier('/home/epwalker97/Python OpenCV files/OpenCV_pythonFiles/haarcascades/haarcascade_frontalface_default.xml')


while True: #infinite loop to run camera
    ignore, frame = camera.read() #read a fram from camera
    frameGray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #converts frame from colors to gray for easier processing
    faceRecFaces=faceCascadeObject.detectMultiScale(frameGray,1.3,5) #detects faces and puts their position in the variable facRecFaces. args: reads from frameGray, sensitivity scale (1.3 is general worls good), unknown parameter but 5 works good, research that parameter if needed
    for faces in faceRecFaces:
        x,y,w,h=faces #positional tracking points for face(s) detected
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3) #creates dimensions of rectangle based off positional points of face given by model, color, thickness
        print('x = ', x, 'y = ',y,'width = ',w,'height = ',h)
    #print(faceRecFaces) #this line will print the position of the faces if desired
    cv2.imshow('Camera', frame) #from camera show frame (first argument is just naming the camera window, can be anything)
    if cv2.waitKey(1) == ord('q'):  #waits 1 ms (waitkey arg) and sees if ordinance (value) of q is pressed. If is then breaks out of while loop. note that & 0xff could need to be between waitkey func and == on certain systems such as windows
        break
camera.release() #releases camera