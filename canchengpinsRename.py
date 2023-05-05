'''
本版解决SMA440U-城中往事三次正则后是sma440U,去掉U
'''

import re
import pyperclip


temp = pyperclip.paste()

#temp = ''''''



first_list = temp.strip().split('\n')

#不能匹配的列表abnormal_list
abnormal_lists = []
abnormal_list1s = []

file1 = open('F:\\a00nutstore\\fishc\\产成品标准命名.txt','w',encoding = 'utf-8')
file2 = open('F:\\a00nutstore\\fishc\\产成品异常明细.txt','w',encoding = 'utf-8')

def canchengpin_rename(first_list):
    global cw_names
    cw_names = []

    for int_string in first_list:

        if int_string =='':
            cw_name = ''
            cw_names.append(cw_name)

        else :
            if int_string[0]=='R':
                print(int_string)
                pattern = r'(-卡面)\s?$'
                regexp = re.compile(pattern)
                mat = regexp.search(int_string)
                if mat == None:
                    print(int_string)
                    pattern = r'(-牛卡)\s?$'
                    regexp = re.compile(pattern)
                    mat = regexp.search(int_string)
                    if mat == None:
                        print(int_string)
                        pattern = r'(\w*-*\d*\w*)(?:-*\w*)'
                        regexp = re.compile(pattern)
                        mat = regexp.search(int_string)

                        if mat == None:
                            print(int_string)
                            cw_name = int_string
                            cw_names.append(cw_name)
                            abnormal_lists.append(cw_name)

                        else:
                            cw_name = mat.group(1)
                            cw_names.append(cw_name)

                    else:
                        print(int_string)
                        cw_name = re.sub(mat.group(1), '牛卡', int_string)
                        print(cw_name)
                        cw_names.append(cw_name)

                else:
                    print(int_string)
                    cw_name = re.sub(mat.group(1),'卡面',int_string)
                    print(cw_name)
                    cw_names.append(cw_name)



            else:
                print(int_string)
                pattern = r'(\w*-*)(?:[\u4e00-\u9fa5]*)(\w*\d*)(?:-*\w*)'
                regexp = re.compile(pattern)
                mat = regexp.search(int_string)
                if mat == None:
                    print(int_string)
                    cw_name = int_string
                    cw_names.append(cw_name)
                    abnormal_lists.append(cw_name)
                else:
                    print(int_string)
                    cw_name = mat.group(1)+mat.group(2)
                    cw_names.append(cw_name)




        print(cw_name)




canchengpin_rename(first_list)


#下面是第二次处理
cw_name1s = []

for cw_name in cw_names:

    if cw_name == '':
        cw_name1 = ''
        cw_name1s.append(cw_name1)

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
                    cw_name1s.append(cw_name)
                    abnormal_list1s.append(cw_name)
                else:
                    cw_name1 = mat.group(1)
                    cw_name1s.append(cw_name1)


            else:
                cw_name1 = mat.group(1)
                cw_name1s.append(cw_name1)



        else:
            cw_name1 = mat.group(1)
            cw_name1s.append(cw_name1)



cw_Newnames =[]

#第三次正则，去掉-
for cw_name1 in cw_name1s:

    if cw_name1 == '':
        cw_Newname = ''
        cw_Newnames.append(cw_Newname)

    else:
        pattern = r'-'
        regexp = re.compile(pattern)
        mat = regexp.search(cw_name1)
        if mat == None:
            cw_Newname = cw_name1
            cw_Newnames.append(cw_Newname)
        else:
            cw_name1 = regexp.sub('', cw_name1)
            pattern = r'(.*?)(?=[a-mo-zA-MO-Z]横?\s?$)'
            regexp = re.compile(pattern)
            mat = regexp.search(cw_name1)
            if mat == None:
                cw_Newname = cw_name1
                cw_Newnames.append(cw_Newname)
                abnormal_list1s.append(cw_Newname)
            else:
                cw_Newname = mat.group(1)
                cw_Newnames.append(cw_name1)



    file1.write('%s\n' % cw_Newname.strip())
    print(cw_Newname)

# 打印没有匹配的产成品名称
print('**********************')
print('下面是没有匹配的产成品：')
for abnormal_list1 in abnormal_list1s:
    file2.write('%s\n' % abnormal_list1)
    print(abnormal_list1)
file1.close()
file2.close()









