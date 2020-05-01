import cv2

face_cascade = cv2.CascadeClassifier('C:\\Users\\DIPESH KUMAR\\AppData\\Local\\Programs\\Python\\Python37-32\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:\\Users\\DIPESH KUMAR\\AppData\\Local\\Programs\\Python\\Python37-32\\Lib\\site-packages\\cv2\\data\\haarcascade_eye.xml')

#face_cascade.load('haarcascade_frontalface_default.xml')
#eye_cascade.load('harrcascade_eye.xml')
    
	
video_capture=cv2.VideoCapture(0)

while True:
    ret,frame=video_capture.read()

    if ret==False:
        continue
    
    
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #canvas=detect(gray, frame)
    faces = face_cascade.detectMultiScale(frame, 1.1, 5)
    
    #print("FACES: ",faces)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
        #roi_gray=gray[y:y+h,x:x+w]
        #roi_color=frame[y:y+h,x:x+w]
    
    
    cv2.imshow('Video',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()

