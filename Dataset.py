import cv2
from os import listdir, mkdir, getcwd
from os.path import isdir, isfile
import sys

name = input("What's your name : ").strip().lower()
if name == '':
    print('Cancel')
    sys.exit()
path = getcwd()+'\\'
path_photo = path + 'Photo_face\\'
path_yml = path + 'Train_dataset'
lsdir = [dir for dir in listdir(path_photo) if isdir(path_photo+dir)]
lsyml = [yml for yml in listdir(path_yml) if isfile(path_yml+'\\'+yml)]
path_name = path_photo+name
if name not in lsdir:
    mkdir(path_name)
    face_count = 0
if name + '.yml' in lsyml: mkdir(path_yml + '\\' + name)

if name in lsdir:
    if len(listdir(path_name)) == 0:
        face_count = 0
    else:
        file = listdir(path_name)
        face_count = max([int(file[i][len(name):-4]) for i in range(len(file))])
x = y = w = h = 0
face_detect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)
while True:
    ret, cap = cam.read()
    gray = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)
    face_detection = face_detect.detectMultiScale(gray, 1.3, 5)
    key = cv2.waitKey(1)
    if face_detection is not ():
        for (x,y,h,w) in face_detection:
            pass
    if key == 99:
        if face_detection is not ():
            face_count += 1
            capture = cap[y:y+h, x:x+w]
            resized_frame = cv2.resize(capture, (250,250))
            gray_re = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
            save = path_name + '\\' + name + str(face_count) + '.jpg'
            cv2.imwrite(save, gray_re)
            cv2.putText(gray_re, str(face_count), (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
            cv2.imshow('your face', gray_re)
        else: print('Face not found!!')
    if face_detection is not (): cv2.rectangle(cap, (x,y), (x+w,y+h), (0,0,255), 5)
    cv2.imshow('cam', cap)
    if key == 27:
        break
cam.release()
cv2.destroyAllWindows()
print(f"All cropped faces are saved in Photo_face\{name} folder")