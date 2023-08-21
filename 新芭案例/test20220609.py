# _*_ coding:utf-8 _*_
# 开发者：小丽的老公
# 开发时间：2022/5/20 22:24
# 开发工具: PyCharm
import pandas as pd

df=pd.read_excel("销售业绩表.xlsx",sheet_name="4月业绩表")
print("标记A\n",df)
"""
       Name       Date     A     B     C     D
0    Name_1 2021-04-01  1918   697  1567   493
1    Name_1 2021-04-01   624  1055  1577   910
2    Name_3 2021-04-02   250  1245   574   713
3    Name_1 2021-04-02  1160   452   810  1024
4    Name_4 2021-04-02  1346   325   950   617
..      ...        ...   ...   ...   ...   ...
95   Name_9 2021-04-29   142  1033  1511   727
96   Name_5 2021-04-30   491  1902   858   187
97   Name_8 2021-04-30   494  1085   815   146
98   Name_4 2021-04-30  1029  1282  1573  1396
99  Name_10 2021-04-30  1685  1594   947   480

[100 rows x 6 columns]
"""
#选择1列,返回一个Series
print("标记B\n",df["Name"])
"""
0      Name_1
1      Name_1
2      Name_3
3      Name_1
4      Name_4
       ...   
95     Name_9
96     Name_5
97     Name_8
98     Name_4
99    Name_10
Name: Name, Length: 100, dtype: object <class 'pandas.core.series.Series'>
"""

#选择1列,返回一个DataFrame,注意同上面的区别，多一对中括号
print("标记C\n",df[["Name"]])
"""
       Name
0    Name_1
1    Name_1
2    Name_3
3    Name_1
4    Name_4
..      ...
95   Name_9
96   Name_5
97   Name_8
98   Name_4
99  Name_10

[100 rows x 1 columns] <class 'pandas.core.frame.DataFrame'>
"""
#选择多列,返回一个DataFrame
print("标记D\n",df[["Name","A","B","C","D"]])
"""
       Name     A     B     C     D
0    Name_1  1918   697  1567   493
1    Name_1   624  1055  1577   910
2    Name_3   250  1245   574   713
3    Name_1  1160   452   810  1024
4    Name_4  1346   325   950   617
..      ...   ...   ...   ...   ...
95   Name_9   142  1033  1511   727
96   Name_5   491  1902   858   187
97   Name_8   494  1085   815   146
98   Name_4  1029  1282  1573  1396
99  Name_10  1685  1594   947   480

[100 rows x 5 columns]
"""

#将DataFrame转成二维列表,读取列表前10行
list=(df.values)
print("标记E\n",list[:10])
"""
[['Name_1' Timestamp('2021-04-01 00:00:00') 12 15 20 7]
 ['Name_1' Timestamp('2021-04-01 00:00:00') 17 18 20 7]
 ['Name_3' Timestamp('2021-04-02 00:00:00') 19 8 15 9]
 ['Name_1' Timestamp('2021-04-02 00:00:00') 19 11 14 7]
 ['Name_4' Timestamp('2021-04-02 00:00:00') 14 16 5 16]
 ['Name_6' Timestamp('2021-04-02 00:00:00') 18 10 19 13]
 ['Name_4' Timestamp('2021-04-03 00:00:00') 19 20 9 9]
 ['Name_2' Timestamp('2021-04-03 00:00:00') 9 6 8 9]
 ['Name_9' Timestamp('2021-04-03 00:00:00') 13 9 14 7]
 ['Name_1' Timestamp('2021-04-03 00:00:00') 20 12 8 15]]

"""

#获取df列索引
cols=df.columns
print("标记F\n",cols)#
# print("标记G\n",list(df))

print("标记H\n",type(df))#

