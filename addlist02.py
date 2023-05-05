'''
本模块计算先计算两个列表去重后的清单，再将这个清单与分别与去重后的列表1和列表2比较，分别计算两个列表中所没有的元素
'''
# _*_ condind = utf-8 _*_
import cangkutotal
import addlists
import chaiwutotal

qichu_dic, ruku_dic, caigou_dic, banchengpin_dic, chuku_dic, lingliao_dic, qimo_dic, taitou_lists,cangkucailiaolist1 = cangkutotal.cangkuTotal()
list1 =cangkucailiaolist1
list2 =chaiwutotal.chaiwuTotal()
print(list2)

addlists.addLists(list1,list2)



