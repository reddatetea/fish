import pandas as pd

def gen_data(n):
    data = [] # 存入每次排班的数据
    lst = [*'abcdefgh'] # 原始员工及顺序数据
    for i in range(n):
        data.append(lst[:4]) # 排班，排进4人
        lst.extend(lst[:2]) # 前两个人追加到列表后总
        lst = lst[2:] # 删除前两个，下次就不从他们排了
    return data
df = pd.DataFrame(gen_data(30),index=pd.date_range('20220501', periods=30))
print(df)