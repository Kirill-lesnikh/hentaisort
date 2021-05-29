from os import listdir
from os.path import isfile, join, splitext
import re
from collections import Counter

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


####################
# matches: match[here_is_a_match]exclude[ (any-digit)]
# ^(?:(?! \(\d\)$).)*

def remove_copy_mark(file_name):
    pattern = re.compile(r'(\d \(\d\))$|( \(\d\))$')
    exclude_words = ['image']
    for exclude_word in exclude_words:
        if re.sub(pattern, '', file_name).find(exclude_word) == -1:
            print('test1')
            return file_name.split()[0]


def normalize_name(file_name):
    pattern = re.compile(r'[^a-z0-9\-_]')
    return re.sub(pattern, '', file_name)


def count_spaces(string):
    counter = 0
    for sym in string:
        if sym == ' ':
            counter += 1
    return counter


def replace_spaces_by_matches_count(string: str, matches_count: int):
    sym_list = list(string)
    for index, item in enumerate(sym_list):
        if item == ' ':
            sym_list[index] = '_'
            matches_count -= 1
        if matches_count == 0:
            result = ''
            return result.join(sym_list)


def normalize_duplicates_name(string: str):
    return replace_spaces_by_matches_count(string, count_spaces(string)-1)

test_string = 'gu neio rw(2)4 (3)5-yv y5{@ #$%3_#*(&@u (1)'
print(normalize_duplicates_name(test_string))
