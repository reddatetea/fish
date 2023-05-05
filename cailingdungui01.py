'''
快查令吨互算
本版增加只传入两个参数，就只判断正度和大度
'''
import pyperclip
import sys
import re
import easygui

msg = '请点选要查询的按钮'
title = '湖北双佳纸品有限公司'
choices = [ '克重', '长', '宽', '令数','吨数']
choice = easygui.buttonbox(msg,title = title,choices = choices)
order =['01','02','03','04','05']
choices_order =dict(zip(choices,order))
order_choices = dict(zip(order,choices))
values = dict(zip(choices,['ke','chang','kuan','ling','dun']))
choices_x =  list(set(choices)-set([choice]))
choices_x.sort()
_ = [choices_order[j] for j in choices_x]
_.sort()
choices_x_order = [order_choices[k] for k in _]
msg = ' 为计算{}请填写相关数据'.format(choice)
value0 = '{}'.format(values[choices_x_order[0]])    #'ke'
value1 = '{}'.format(values[choices_x_order[1]])
value2 = '{}'.format(values[choices_x_order[2]])
value3 = '{}'.format(values[choices_x_order[3]])
values = [value0,value1,value2,value3]
v0,v1,v2,v3 = easygui.multenterbox(msg,fields=choices_x_order)
vs = [v0,v1,v2,v3]
for i in range(len(values)):         #将字符串名作为变量
    m = values[i]
    n = vs[i]
    exec(f"{m} = n")
if choice == '吨数':
    dun = float(ke)/1000/1000*float(chang)/1000*float(kuan)/1000*500*float(ling)
    print(dun)
elif choice == '令数':
    ling = float(dun)/float(ke)*1000*1000/float(chang)*1000/float(kuan)*1000/500
    print(ling)
elif choice == '克重':
    ke = float(dun)/float(ling)/500*1000/float(chang)*1000/float(kuan)*1000*1000
    print(ke)
elif choice == '长':
    chang = float(dun)*float(ling)/float(ke)*1000*1000/float(kuan)*1000/500/1000
    print(chang)
else :
    kuan = float(dun)*float(ling)/float(ke)*1000*1000/float(chang)*1000/500/1000
    print(kuan)

