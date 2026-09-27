import cv2
import mediapipe as mp
# print(cv2.__version__)
width=640
height=420
camera = cv2.VideoCapture(1,cv2.CAP_DSHOW) #makes camera object and uses video function with the camera in use as argument (typically 0-4 depending on port camera is plugged into)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, width) #sets camera window width
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height) #sets camera window height
camera.set(cv2.CAP_PROP_FPS, 30)
camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
handsObject=mp.solutions.hands.Hands(False,2,.5,) #this is methods for analyzing frame for hand tracking and detection: first argument asks if it is a still image (False since using video), second argument is how many hands to look for(2), third and fourth arguments is how confident in tracking does it need to be (0.5)
mpDraw = mp.solutions.drawing_utils #annotates frame with data from hands(above)

while True: #infinite loop to run camera
    ignore, frame = camera.read() #read a fram from camera
    frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)  #converts bgr to rgb
    results = handsObject.process(frameRGB)
    cv2.imshow('Camera', frame) #from camera show frame (first argument is just naming the camera window, can be anything)
    if cv2.waitKey(1) == ord('q'):  #waits 1 ms (waitkey arg) and sees if ordinance (value) of q is pressed. If is then breaks out of while loop. note that & 0xff could need to be between waitkey func and == on certain systems such as windows
        break
camera.release() #releases camera