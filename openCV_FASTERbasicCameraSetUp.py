import cv2
# print(cv2.__version__)
width=640
height=420
camera = cv2.VideoCapture(1,cv2.CAP_DSHOW) #makes camera object and uses video function with the camera in use as argument (typically 0-4 depending on port camera is plugged into)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, width) #sets camera window width
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height) #sets camera window height
camera.set(cv2.CAP_PROP_FPS, 30)
camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
while True: #infinite loop to run camera
    ignore, frame = camera.read() #read a fram from camera
    cv2.imshow('Camera', frame) #from camera show frame (first argument is just naming the camera window, can be anything)
    if cv2.waitKey(1) == ord('q'):  #waits 1 ms (waitkey arg) and sees if ordinance (value) of q is pressed. If is then breaks out of while loop. note that & 0xff could need to be between waitkey func and == on certain systems such as windows
        break
cam.release() #releases camera


#ALL PROGRAMS CURRENTLY SAVED UP TO THE USE OF MEDIAPIPE DO NOT =>
# => USE THIS FASTER METHOD OF OPENING CAMERA, BE SURE TO CHANGE AS =>
# => YOU USE THEM!!!!!!!!!!!!!!!
