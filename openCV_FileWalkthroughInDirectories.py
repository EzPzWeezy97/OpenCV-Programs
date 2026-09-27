import os
import cv2
import face_recognition as FR

imageDirectory = '/home/epwalker97/Python_OpenCV_files/OpenCV_pythonFiles/demoImages/known' # THIS IS SOURCE WHERE START WALKrecognize that some Op Systems us \ slashes instead

for myPresentFolder , directories, files in os.walk(imageDirectory): # loops through folder and its what it contains and prints them
    print('My working folder (myPresent Folder): ' , myPresentFolder)
    print('Directories in working folder: ', directories )
    print('My files in working folder: ' , files)
    for file in files:
        print('Your guy is: ', file)
        fullFilePath = os.path.join(myPresentFolder, file) #gives us the path to each file walked through
        print(fullFilePath)
        name = os.path.splitext(file)[0] #seperates .jpg from file name into an array where the name is first iem in array and the.jpg is the second item in array (0 indexed)so we can just have their name from the file
        print(name)
        myPicture=FR.load_image_file(fullFilePath)
        myPicture = cv2.cvtColor(myPicture, cv2.COLOR_RGB2BGR)
        cv2.imshow(name, myPicture)
        cv2.waitKey(2500)
        cv2.destroyAllWindows()

        #THIS PROGRAM CURRENTLY WALKS THROUGH EACH PHOTO FILE IN THIS DIRECTORY AND SHOWS THEM WITH THEIR NAME FOR 2.5 SEC