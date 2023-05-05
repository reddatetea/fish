# *_* coding :utf-8 *_*
import  easygui

gongyingshangs = [1,2,3,4,5,6]
gongyingshang_xuhaos = []
for i in range(len(gongyingshangs)):
    print('{}--{}\n'.format(i,gongyingshangs[i]))
    gongyingshang_xuhaos.append(str(i))
print(gongyingshang_xuhaos)
msg = '请选择供应商序号'
gongyingshang_xuhao = easygui.buttonbox(msg, title=msg, choices=gongyingshang_xuhaos)
gongyingshang = gongyingshangs[int(gongyingshang_xuhao)]
print(gongyingshang)
