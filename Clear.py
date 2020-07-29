from os import listdir, remove, rmdir, getcwd
from os.path import isdir, exists, join
import sys

path = getcwd()+'\\'
path_photo = path + 'Photo_face'
path_yml = path + 'Train_dataset'
lsdir = [dir for dir in listdir(path_photo)]
name = []

def clear(folder):
    global path
    path_folder = path + folder
    for f in listdir(path_folder):
        if isdir(path_folder+'\\'+f): rmdir(path_folder+'\\'+f)
        else: remove(path_folder+'\\'+f)
def clear_name(name):
    global path
    global path_photo
    global path_yml
    if exists(join(path_photo, name)):
        for i in listdir(join(path_photo, name)):
            remove(join(path_photo, name, i))
        rmdir(join(path_photo, name))
    if exists(join(path_yml, name+'.yml')): remove(join(path_yml, name+'.yml'))        

while True:
    name_in = input('Who do you want delete? (name or ALL) : ').strip()
    if name_in == 'ALL':
        for i in listdir(path_photo):
            clear('photo_face\\'+i)
            rmdir(path + 'Photo_face\\'+i)
        clear('Train_dataset')
        print('success')
        sys.exit()
    elif name_in == '': break
    elif name_in in lsdir: name.append(name_in)
    else: print('Not found user')

for n in name: clear_name(n)

print('success')