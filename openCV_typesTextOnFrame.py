import cv2
# print(cv2.__version__)
width=640
height=420
message = "DO U C ME?"
camera = cv2.VideoCapture(0) #makes camera object and uses video function with the camera in use as argument (typically 0-4 depending on port camera is plugged into)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, width) #sets camera window width
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height) #sets camera window height
while True: #infinite loop to run camera
    ignore, frame = camera.read() #read a frame from camera
    #frame[180:240,280:360]=(255,0,255) #basically givig an area of pixels to manipulate, first argument is range of rows(in pixels on window) you will manipulate and second is range of columns(for height) then = (x,x,x) is how we manupulate those in colors BGR (0-255)
    #cv2.rectangle(frame,(280,180),(360,240),(255,100,160),2) #for putting rectangles on screen, arugements are as follows: frame, point of top left corner given in (x,y) values, point of bottom right corner also (x,y), color manipulation in BGR, line thickness
    #cv2.circle(frame,(320,210),25,(0,0,0),2) #for putting cirlces on screen args as follows: frame, point for center of cirlce, radius in pixels, color, width. NOTe! if want to use width/2 or height/2 must wrap as an int 
    cv2.putText(frame,message,(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2) # for putting text on screen args as follows: frame, text, x,y coordinate, font, font size, color (bgr),heaviness of font 
    cv2.imshow('Camera', frame) #from camera show frame (first argument is just naming the camera window, can be anything)
    if cv2.waitKey(1) == ord('q'):  #waits 1 ms (waitkey arg) and sees if ordinance (value) of q is pressed. If is then breaks out of while loop. note that & 0xff could need to be between waitkey func and == on certain systems such as windows
        break
cam.release() #releases camera