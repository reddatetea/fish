'''
对某序列进行排序(默认升序,降序时第二参数选True),
并获取其顺序前的序列号,
可用于openpyxl库,方便对指定列排序
'''
def sorted_yuanxuhao(iterable,sort_way = False):
    yxh = len(iterable)
    lst1 = list(zip(iterable, range(yxh)))
    lst2 = sorted(lst1, key=lambda x: x[0],reverse = sort_way)      #如降序则reverse = True
    lst3 = list(zip(*lst2))
    new_xhs = lst3[-1]
    return new_xhs

def main():
    a = [5,2,2,4,3]
    nxh = sorted_yuanxuhao(a,True)
    print(nxh)

if __name__ == '__main__':
    main()

