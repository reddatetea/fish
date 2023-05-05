'''
本版解决SMA440U-城中往事三次正则后是sma440U,去掉U
'''

import re

def canchengpinrename(int_string):
    if int_string  in ['',None]:
        cw_name = ''

    else:
        if int_string[0] == 'R':
            pattern = r'(-卡面)\s?$'
            regexp = re.compile(pattern)
            mat = regexp.search(int_string)
            if mat == None:
                pattern = r'(-牛卡)\s?$'
                regexp = re.compile(pattern)
                mat = regexp.search(int_string)
                if mat == None:
                    pattern = r'(\w*-*\d*\w*)(?:-*\w*)'
                    regexp = re.compile(pattern)
                    mat = regexp.search(int_string)

                    if mat == None:
                        cw_name = int_string

                    else:
                        cw_name = mat.group(1)

                else:
                    cw_name = re.sub(mat.group(1), '牛卡', int_string)

            else:
                cw_name = re.sub(mat.group(1), '卡面', int_string)


        else:
            pattern = r'(\w*-*)(?:[\u4e00-\u9fa5]*)(\w*\d*)(?:-*\w*)'
            regexp = re.compile(pattern)
            mat = regexp.search(int_string)
            if mat == None:
                cw_name = int_string

            else:
                cw_name = mat.group(1) + mat.group(2)


    #下面是第二次处理

    if cw_name in ['',None]:
        cw_name1 = ''

    else:
        # 777-1类似
        pattern = r'(.*?)(?=-\d$)'
        regexp = re.compile(pattern)
        mat = regexp.search(cw_name)
        if mat == None:
            # DJL48混装1类似
            pattern = r'(.*?)(?=混装①?②?\d*$)'
            regexp = re.compile(pattern)
            mat = regexp.search(cw_name)
            if mat == None:
                # 最后是不为N的单字符
                pattern = r'(.*?)(?=[a-mo-zA-MO-Z]横?\s?$)'
                regexp = re.compile(pattern)
                mat = regexp.search(cw_name)
                if mat == None:
                    cw_name1 = cw_name

                else:
                    cw_name1 = mat.group(1)

            else:
                cw_name1 = mat.group(1)

        else:
            cw_name1 = mat.group(1)


    #第三次正则，去掉-

    if cw_name1 in ['',None]:
        cw_Newname = ''
    else:
        pattern = r'-'
        regexp = re.compile(pattern)
        mat = regexp.search(cw_name1)
        if mat == None:
            cw_Newname = cw_name1
        else:
            cw_name1 = regexp.sub('', cw_name1)
            pattern = r'(.*?)(?=[a-mo-zA-MO-Z]横?\s?$)'
            regexp = re.compile(pattern)
            mat = regexp.search(cw_name1)
            if mat == None:
                cw_Newname = cw_name1
            else:
                cw_Newname = mat.group(1)

    print(cw_Newname)
    return cw_Newname


def main():
    int_string = 'DL-3280-远方的世界'
    canchengpinrename(int_string)


if __name__ == '__main__':
    main()



