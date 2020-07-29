import cv2
from os import listdir, getcwd
from os.path import isfile, join
import numpy as np

path = getcwd()+'\\'
path_yml = path + 'Train_dataset'
ls_yml = [f for f in listdir(path_yml) if isfile(join(path_yml, f))]
ls_name = [n[:-4] for n in ls_yml]
dict_name = {}
for i, yml in enumerate(ls_yml):
    dict_name[ls_name[i]] = cv2.face.LBPHFaceRecognizer_create()
    dict_name[ls_name[i]].read(join(path_yml, yml))
if dict_name == {}: dict_name['empty'] = 100
name = list(dict_name.keys())

face_detect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def face_detector(gray):
    coordination_face = [0,0,0,0]
    face_detection = face_detect.detectMultiScale(gray, 1.3, 5)
    if face_detection is ():
        return []
    return face_detection

alert = 0
cam = cv2.VideoCapture(0)
while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    coordination_face = face_detector(gray)
    if coordination_face != []:
        try:
            for [x,y,w,h] in coordination_face:
                matching = []
                face = gray[y:y+h, x:x+w]
                face = cv2.resize(face, (250,250))
                for t in dict_name.values():
                    if dict_name == {'empty':100}: matching = [[0,100]]
                    else:
                        match = t.predict(face)
                        matching.append(match)
                max_match = 100
                for n, m in enumerate(matching):
                    if m[1] < 50 and m[1] < max_match:
                        max_match = m[1]
                        face_name_number = n
                        col = (0,255,0)
                        alert = 0
                    elif max_match == 100 and n == len(dict_name.values())-1:
                        col = (0,0,255)
                        alert += 1
                if max_match != 100:
                    cv2.putText(img, name[face_name_number], (x,y-10), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,255), 2)
                else: cv2.putText(img, 'Not found', (x,y-10), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
                cv2.rectangle(img, (x,y), (x+w, y+h), col, 4)
                cv2.imshow('Real-time Face Recognition', img)
        except: 
            cv2.imshow('Real-time Face Recognition', img)
    if alert > 100:
        alert += 1
        cv2.putText(img, 'Alert', (110,400), cv2.FONT_HERSHEY_COMPLEX, 5, (0,0,255), 5)
        if alert >= 150: alert -= 70
        if cv2.waitKey(1) == 99: 
            alert = 0
            print('Cancel and Realert')
        cv2.imshow('Real-time Face Recognition', img)
    else: cv2.imshow('Real-time Face Recognition', img)
    if cv2.waitKey(1) == 27: break
cam.release()
cv2.destroyAllWindows()