# -*- coding:utf-8 -*-
import re
import openpyxl


with open('C:\\Users\\asus\\dal\\fishc\\abc.txt','r',encoding='utf-8') as file :
    dataMat=[]
    for imput_str in file.readlines() :
        #去除字符串中间的空格
        #print(imput_str)
        temp = imput_str.split()
        imput_str = ' '.join(temp)
        dataMat.append(imput_str)
print(dataMat)

wb = openpyxl.load_workbook('东山头园区企业拟返工人员统计表.xlsx')

# 选择默认的工作表
ws = wb.active

# 给工作表重命名
ws.title = '双佳仓库及财务信息表'

# 写入一行数据
#row = ['序号','姓名','年龄','性别','电话','身份证号', '序号','现居住所在地','是否有已满14天的健康检测证明','是否与确诊患者或疑似新冠肺炎患者有过接触','备注']
#sheet.append(row)

def getrow():
    for imput_str in dataMat:
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

        rowlist = ['',name,age,gender,phonenumber,idcard,'',address]
    return rowlist


for index, row in enumerate(ws.values):
    if index != 3:
        print(row)
        continue
    else :
        getrow()
        print(row)
        ws.append(rowlist)


wb.save('fangong03.xlsx')



































