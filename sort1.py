from os import listdir
from os.path import isfile, join, splitext

# main_path = 'Z:\\usb\\USB\\[_Art]'
main_path = 'Z:\\usb\\USB\\[_Art]\\0test'
files = [splitext(f)[0] for f in listdir(main_path) if isfile(join(main_path, f))]
filesDict = {}
lastElementIndex = -1
iteraiton = 0
stopper = len(files)

for i in range(len(files)):
    if i <= lastElementIndex:
        continue
    iterator = 1
    tempArr = [files[i]]
    while True:
        iteraiton += 1
        if iteraiton > stopper:
            break
        if iterator + i >= len(files):
            break
        nextFile = files[i+iterator]
        if files[i] == nextFile[:len(files[i])] and len(files[i]) > 2:
            iterator += 1
            tempArr.append(nextFile)
        else:
            filesDict[tempArr[0]] = tempArr
            lastElementIndex = files.index(nextFile) - 1
            break

for key in filesDict.keys():
    if len(filesDict[key]) > 1:
        print(key + ": " + str(filesDict[key]))
