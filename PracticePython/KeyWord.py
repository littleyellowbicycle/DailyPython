import os.path
import collections


def judgeit(words):
    for i in range(6):
        if len(words[i]
               ) > 2 and words[i] != 'the' and words[i] != 'her' and words[
                   i] != 'his' and words[i] != 'and' and words[i] != 'she':
            return words[i]
    return words[7]


def findkeys(dirPath):
    if (os.path.exists(dirPath)):
        print("obj path is: " + os.path.realpath(dirPath))
    f_list = os.listdir(dirPath)
    for f in f_list:
        if os.path.splitext(f)[1] == '.py':
            print("the key word of %s is: " % f)
            with open(f, 'r', encoding='UTF-8') as fp:
                strText = fp.read().split(' ')
            b = collections.Counter(strText)
            words = sorted(b, key=lambda x: b[x], reverse=True)
            print(judgeit(words))


findkeys(".\\")
