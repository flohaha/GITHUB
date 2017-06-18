import os
from shutil import copyfile

root = os.getcwd()
print root

dst = root + '/Pics_Gathered/'
print dst

os.chdir('Pics')
new_dir = os.getcwd()
print new_dir


for subdir, dirs, files in os.walk(".", topdown=False):
    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file
        print filepath

        if file.endswith(".jpg"):
            print (file)
            copyfile(filepath, dst +  '/' + file)
