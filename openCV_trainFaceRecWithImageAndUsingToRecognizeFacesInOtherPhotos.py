import cv2
import face_recognition as faceRec
font = cv2.FONT_HERSHEY_SIMPLEX
donTrumpFace=faceRec.load_image_file('/home/epwalker97/Python OpenCV files/OpenCV_pythonFiles/demoImages/known/Donald Trump.jpg') #image of just Donald for training data
faceLocation = faceRec.face_locations(donTrumpFace)[0] #has the [0] becasue this is an array of arrays and since theres only one face we just need the first one
donTrumpFaceEncode=faceRec.face_encodings(donTrumpFace)[0] #this basically trains to recognize this face (encodes the data for face)

nancyPelFace=faceRec.load_image_file('/home/epwalker97/Python OpenCV files/OpenCV_pythonFiles/demoImages/known/Nancy Pelosi.jpg') #Image of just nancy for training data
faceLocation = faceRec.face_locations(nancyPelFace)[0] #has the [0] becasue this is an array of arrays and since theres only one facewe just need the first one
nancyPelFaceEncode=faceRec.face_encodings(nancyPelFace)[0] #this basically trains to recognize this face (encodes the data for face)

knownEncodings = [donTrumpFaceEncode,nancyPelFaceEncode] #array of recognizable faces
names = ['Donald Trump', 'Nancy Pelosi'] #array of names of recognizable faces (must be in same order as knownEncodings array)

unknownFace =  faceRec.load_image_file('/home/epwalker97/Python OpenCV files/OpenCV_pythonFiles/demoImages/unknown/u3.jpg') #image with unknown faces (change to u1.jpg if want to try with 1 trump face and 3 unknowns)
unknownFaceBGR = cv2.cvtColor(unknownFace,cv2.COLOR_RGB2BGR) #converts image to BGR
faceLocations = faceRec.face_locations(unknownFace) #face locations function on image
unknownEncodings = faceRec.face_encodings(unknownFace, faceLocations) #encoding data of the unkown faces in image

for faceLocation, unknownEncoding in zip(faceLocations, unknownEncodings): #loops through the face locations and encodings and tries to identify them with our known encodins
    top,right,bottom,left = faceLocation
    print(faceLocation)
    cv2.rectangle(unknownFaceBGR, (left,top),(right,bottom), (255,0,0),3)
    name = 'Unknown person'
    matches = faceRec.compare_faces(knownEncodings, unknownEncoding) #our matches with encodings (BOOLEAN OUTPUT)
    print(matches)
    if True in matches: #prints our matches if found
       matchIndex = matches.index(True)
       print(matchIndex)
       print(names[matchIndex])
       name = names[matchIndex]
    
    cv2.putText(unknownFaceBGR,name,(left,top),font,1,(0,0,255),2) #puts name on rectangle 

cv2.imshow('My Faces', unknownFaceBGR)

cv2.waitKey(5000)


