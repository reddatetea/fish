'''
指定inercept截距 num步长 delimiter分隔符
对字符串进行分隔
'''
def intercept(s,num,delimiter):     #inercept截距 num每段长度 delimiter分隔符
    s1=str(s) #将要分段的对象转换为字符串类型。
    lst=[s1[n:n+num] for n in range(0,len(s1),num)] #对数据进行分段处理。
    s2=delimiter.join(lst) #合并分段的列表。#用指定的分隔符合并分段的列表各元素，形成一个新的字符串
    return s2 #将合并结果返回函数。

def  main():
    s = '白日依山尽黄河入海流欲穷千里目更上一层楼'
    num = 5
    delimiter = '，'
    s2 = intercept(s, num, delimiter)
    print(s2)

if __name__ == '__main__':
    main()