import zhigongyingshang
import pprint
import easygui

def chaxunTianjia():
    new_gongyingshang = input('请输入新供应商名字:\n')
    if new_gongyingshang not in gongyingshang_dic:
        print('该供应商不在原供应商列表中')
        new_jianchen = input('请输入"{}"的简称\n'.format(new_gongyingshang))
        gongyingshang_dic[new_gongyingshang] = new_jianchen
    else:
        print('该供应商已在原供应商列表中,不需要添加')

gongyingshang_dic = zhigongyingshang.jianchen
jieshuchaxun = True
while jieshuchaxun :

    msg = '查询和新增纸供应商'
    print(msg)
    choice = easygui.ccbox(msg, title='继续查询和添加or退出', choices=('yes', 'no'))
    if choice == True :
        chaxunTianjia()
    else :
        jieshuchaxun = False

with open('zhigongyingshang.py','w',encoding='utf-8') as f:
    f.write('jianchen = ' + pprint.pformat(gongyingshang_dic))
