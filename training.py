import cv2
import os
import numpy as np
from PIL import Image
def Train():
 #recognizer = cv2.createLBPHFaceRecognizer()
 recognizer = cv2.face.LBPHFaceRecognizer_create()
 path="dataset"
 def getImagesWithID(path):
    ImagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    faces=[]
    IDs=[]
    for ImagePath in ImagePaths:
        faceImg=Image.open(ImagePath).convert('L')
        faceNp=np.array(faceImg,'uint8')
        ID=int(os.path.split(ImagePath)[-1].split('.')[1])
        faces.append(faceNp)
        IDs.append(ID)
        #cv2.imshow("trainning",faceNp)
        #cv2.waitKey(10)
    return np.array(IDs),faces
 Ids,faces=getImagesWithID(path)
 recognizer.train(faces,Ids)
 recognizer.save("recognizer/trainer.yml")
 cv2.destroyAllWindows()

Train() 