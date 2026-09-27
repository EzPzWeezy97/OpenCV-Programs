import cv2
# print(cv2.__version__)
width=640
height=420
camera = cv2.VideoCapture(0) #makes camera object and uses video function with the camera in use as argument (typically 0-4 depending on port camera is plugged into)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, width) #sets camera window width
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height) #sets camera window height
while True: #infinite loop to run camera
    ignore, frame = camera.read() #read a frame from camera
    frame[180:240,280:360]=(255,0,255) #SQUARE/RECTANGLE #first argument is range of rows(in pixels on window) you will manipulate and second is range of columns(for height) then = (x,x,x) is how we manupulate those in colors BGR (0-255)
    cv2.imshow('Camera', frame) #from camera show frame (first argument is just naming the camera window, can be anything)
    if cv2.waitKey(1) == ord('q'):  #waits 1 ms (waitkey arg) and sees if ordinance (value) of q is pressed. If is then breaks out of while loop. note that & 0xff could need to be between waitkey func and == on certain systems such as windows
        break
cam.release() #releases camera