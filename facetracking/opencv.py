import cv2

webcam = cv2.VideoCapture(0)
if not webcam.isOpened():
    raise Exception("Could not open video device")
webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 320) 
webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
frontalface = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
profileface = cv2.CascadeClassifier("haarcascade_profileface.xml")
face = [0,0,0,0]    
Cface = [0,0]       
lastface = 0

while True:

    faceFound = False
    
    if not faceFound:
        if lastface == 0 or lastface == 1:
            aframe = webcam.read()[1]  
            aframe = webcam.read()[1]  
            aframe = webcam.read()[1]  
            aframe = webcam.read()[1]   
            aframe = webcam.read()[1]   
            fface = frontalface.detectMultiScale(aframe,1.3,4,(cv2.CASCADE_DO_CANNY_PRUNING + cv2.CASCADE_FIND_BIGGEST_OBJECT + cv2.CASCADE_DO_ROUGH_SEARCH),(60,60))
            if fface != ():         # if we found a frontal face...
                lastface = 1        # set lastface 1 (so next loop we will only look for a frontface)
                for f in fface:     # f in fface is an array with a rectangle representing a face
                    faceFound = True
                    face = f

    if not faceFound:               # if we didnt find a face yet...
        if lastface == 0 or lastface == 2:  # only attempt it if we didn't find a face last loop or if-
            aframe = webcam.read()[1]   #   THIS method was the one who found it last loop
            aframe = webcam.read()[1]
            aframe = webcam.read()[1]   # again we grab some frames, things may have gotten stale-
            aframe = webcam.read()[1]   # since the frontalface search above
            aframe = webcam.read()[1]
            pfacer = profileface.detectMultiScale(aframe,1.3,4,(cv2.CASCADE_DO_CANNY_PRUNING + cv2.CASCADE_FIND_BIGGEST_OBJECT + cv2.CASCADE_DO_ROUGH_SEARCH),(80,80))
            if pfacer != ():        # if we found a profile face...
                lastface = 2
                for f in pfacer:
                    faceFound = True
                    face = f

    if not faceFound:               # a final attempt
        if lastface == 0 or lastface == 3:  # this is another profile face search, because OpenCV can only-
            aframe = webcam.read()[1]   #   detect right profile faces, if the cam is looking at-
            aframe = webcam.read()[1]   #   someone from the left, it won't see them. So we just...
            aframe = webcam.read()[1]
            aframe = webcam.read()[1]
            aframe = webcam.read()[1]
            cv2.flip(aframe,1,aframe)   #   flip the image
            pfacel = profileface.detectMultiScale(aframe,1.3,4,(cv2.CASCADE_DO_CANNY_PRUNING + cv2.CASCADE_FIND_BIGGEST_OBJECT + cv2.CASCADE_DO_ROUGH_SEARCH),(80,80))
            if pfacel != ():
                lastface = 3
                for f in pfacel:
                    faceFound = True
                    face = f

    if not faceFound:       # if no face was found...-
        lastface = 0        #   the next loop needs to know
        face = [0,0,0,0]    # so that it doesn't think the face is still where it was last loop


    x,y,w,h = face
    Cface = [(w/2+x),(h/2+y)]   # we are given an x,y corner point and a width and height, we need the center
    print str(Cface[0]) + "," + str(Cface[1])

    if Cface[0] != 0:       # if the Center of the face is not zero (meaning no face was found)

        if Cface[0] > 180:  # The camera is moved diffrent distances and speeds depending on how far away-
            print("left1")    #   from the center of that axis it detects a face
        if Cface[0] > 190:  #
            print("left2")    #
        if Cface[0] > 200:  #
            print("left3")    #

        if Cface[0] < 140:  # and diffrent dirrections depending on what side of center if finds a face.
            print("right1")
        if Cface[0] < 130:
            print("right2")
        if Cface[0] < 120:
            print("right3")

        if Cface[1] > 140:  # and moves diffrent servos depending on what axis we are talking about.
            print("down1")
        if Cface[1] > 150:
            print("down2")
        if Cface[1] > 160:
            print("down3")

        if Cface[1] < 100:
            print("up1")
        if Cface[1] < 90:
            print("up2")
        if Cface[1] < 80:
            print("up3")
