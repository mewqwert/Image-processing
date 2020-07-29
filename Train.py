import cv2
from os import listdir, mkdir, remove, rmdir, getcwd
from os.path import isdir, exists, join
import numpy as np
import sys

path = getcwd()+'\\'
path_photo = path + 'Photo_face'
path_yml = path + 'Train_dataset'
lsdir = [dir for dir in listdir(path_photo)]
up = [d for d in listdir(path_yml) if isdir(path_yml + '\\' + d)]
if lsdir == []:
    print("Don't have any photo file")
    sys.exit()

def save_yml(name):
    global path_photo
    global path_yml
    Training, Index = [], []
    path_file = [f for f in listdir(path_photo+'\\'+name)]
    for i, file in enumerate(path_file):
        path_img = path_photo + '\\' + name + '\\' + file
        read = cv2.imread(path_img, 0)
        Training.append(np.asarray(read, dtype=np.uint8))
        Index.append(i)
    Index = np.asarray(Index, dtype=np.int32)
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.train(np.asarray(Training), np.asarray(Index))
    face_recognizer.save(path_yml + '\\' + name + '.yml')
    print(f"Training {name} completed successfully")
def delete(name):
    global path_yml
    rmdir(path_yml + '\\' + name)
    remove(path_yml + '\\' + name + '.yml')

if up != []:
    for n in up:
        delete(n)
        save_yml(n)

file_train = [fn for fn in listdir(path_yml)]
if file_train == []:
    for j in lsdir: save_yml(j)
elif len(file_train) != len(lsdir):
    for k in lsdir:
        if not exists(join(path_yml, k+'.yml')):
            save_yml(k)
            
print('success')