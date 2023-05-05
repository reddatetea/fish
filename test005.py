import easygui

msg = '请输入文件后缀'
target0 = easygui.multenterbox(msg,title='文件后缀',fields=['后缀1','后缀2','后缀3','后缀4','后缀5'])
target = []

for j  in target0 :
    if  j!='':
        target.append('.'+j)
print(target)
