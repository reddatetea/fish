'''
对疑犯追踪的文件进行更名，以配比字幕文件
'''

import re
import os
from easygui import diropenbox

# int_string = r'Person.of.Interest.s01E01.720p.BluRay.X264-REWARD.mkv'

path = diropenbox('请点选要更改名字的文件所在文件夹')
file_lst = [i for i in os.listdir(path) if os.path.isfile(os.path.join(path,i))]

pattern = r'(?:(P|p)erson(.|\.)of(.|\.)(I|i)nterest(.|\.)(s|S)\d{2}(E|e)\d{2})(?P<name>.*)\.(mkv|sub|idx)$'
regexp = re.compile(pattern)

for i in file_lst:
    mat = regexp.search(i)
    if mat:
        new = re.sub(mat.group('name'), '', i)
        old_fname = os.path.join(path, i)
        new_fname = os.path.join(path, new)
        os.rename(old_fname, new_fname)
    else:
        continue

