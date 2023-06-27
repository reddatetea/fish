# -*- coding:utf-8 -*-
import re
from openpyxl import Workbook


with open('C:\\Users\\asus\\dal\\fishc\\abc.txt','r',encoding='utf-8') as file :
    dataMat=[]
    for imput_str in file.readlines() :
        #去除字符串中间的空格
        #print(imput_str)
        temp = imput_str.split()
        imput_str = ' '.join(temp)
        dataMat.append(imput_str)
print(dataMat)

wb = Workbook()

# 选择默认的工作表
sheet = wb.active

# 给工作表重命名
sheet.title = '双佳仓库及财务信息表'

# 写入一行数据
row = ['姓名','年龄','性别','电话','身份证号', '现居住所在地']
sheet.append(row)


for imput_str in dataMat:

    #读取姓名
    imput_re1 = r'^[\u4e00-\u9fa5]{2,3}'
    pattern1 = re.compile(imput_re1)
    res1 = re.search(pattern1,imput_str)
    name = res1.group()
    print(name)

    #读取身份证
    imput_re2 = r'(\d{6})(\d{4})(\d{2})(\d{2})(\d{3})([0-9]|X|x)'
    pattern2 = re.compile(imput_re2)
    res2 = re.search(pattern2,imput_str)
    idcard = res2.group().strip()
    birthYear = int(idcard[6:10])
    age= 2020 - birthYear
    print(len(idcard))
    senventeen = int(idcard[-2])
    if senventeen%2==0 :
        gender = '女'
    else :
        gender = '男'
    print(idcard,age,senventeen,gender)




    #读取住址
    imput_re3 = r'[\u4e00-\u9fa5]{4,30}\w*[\u4e00-\u9fa5]{4,30}\w*[-]*\d*'
    pattern3 = re.compile(imput_re3)
    res3 = re.search(pattern3,imput_str)
    address = res3.group()
    print(address)

    #读取电话号码
    imput_re4 = r'1[0-9]{10}$'
    pattern4 = re.compile(imput_re4)
    res4 = re.search(pattern4,imput_str)
    phonenumber = res4.group()
    print(phonenumber)

    sheet.append([name,age,gender,phonenumber,idcard,address])

wb.save('fangong02.xlsx')






