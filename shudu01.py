import openpyxl
import os
import pandas as pd


def dataReader(fname,ws_name1,ws_name2):
    wb = openpyxl.load_workbook(fname)
    ws1 = wb[ws_name1]
    shudu_range = ws1['A1:I9']
    data = []

    for i in shudu_range:
        hang = []
        for j in i:
            hang.append(j.value)
        data.append(hang)

    print(data)
    wb.save(fname)
    return data


def yunsuan(data):
    man = {1,2,3,4,5,6,7,8,9}
    lies = [k for k in 'ABCDEFGHI']
    hangs = ['r1','r2','r3','r4','r5','r6','r7','r8','r9']
    pd_data = pd.DataFrame(data,columns = lies,index = hangs)
    #print(pd_data)

    #横向，将None替换为行里没有的数的列表
    for i in data :
        hang_youshus = [ j for j in i if j!=None]
        #print(hang_youshus)
        yushus = list(man - set(hang_youshus))
        #print(yushus)

        for index,j in enumerate(i ):
            if j ==None :
                i[index] = yushus

        # 纵向，将有列表与纵列中没有的数取交集
        for i in data:
            hang_youshus = [j for j in i if j != None]
            # print(hang_youshus)
            yushus = list(man - set(hang_youshus))
            # print(yushus)

            for index, j in enumerate(i):
                if j == None:
                    i[index] = yushus

    print(data)


def main():
    fname = r'F:\a00nutstore\fishc\shudu.xlsx'
    ws_name1 = '题目'
    ws_name2 = '答案'
    data = dataReader(fname,ws_name1,ws_name2)
    yunsuan(data)
    #os.system(fname)


if __name__ == '__main__':
    main()
