import collections
import os

with open('139号令修改部分内容.txt', 'r') as fp:
    str1 = fp.read().split(' ')
b = collections.Counter(str1)
with open('result.txt', 'w') as result_file:
    for key, value in b.items():
        result_file.write(key + ':' + str(value) + '\n')
