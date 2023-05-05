'''
本模块计算先计算两个列表去重后的清单，再将这个清单与分别与去重后的列表1和列表2比较，分别计算两个列表中所没有的元素
'''
# _*_ condind = utf-8 _*_


def addLists(list1,list2):

    list1zip=list(set(list1))
    list2zip=list(set(list2))
    listtotal = list(set(list1+list2))

    addList1s = []

    for i in listtotal:
        if i not in list1zip :
            addList1s.append(i)
        else :
            continue
    print(addList1s)

    addList2s = []

    for i in listtotal:
        if i not in list2zip:
            addList2s.append(i)
        else:
            continue
    print(addList2s)
    return addList1s,addList2s

def main():
    a = [1, 2, 3, 3, 4, 5, 6]
    b = [1, 2, 3, 3, 7, 8]

    addLists(a,b)



if __name__ == "__main__":
    main()


