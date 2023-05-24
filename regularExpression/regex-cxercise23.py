# -*- conding = utf-8 -*-
import re

#string = '（乌合之众）：大众心理研究（豆瓣图书Top 250，90818评价，评分8.2，经典畅销版本'
string = '人生的智慧 (叔本华系列)(豆瓣8.7分好评第一译本)'
#string ='人间失格（太宰治灵魂深处无助的生命绝唱 献给迷茫中挣扎的人）'
#string = '面纱(畅销十年、豆瓣8.7分好评第一译本 毛姆剖析人)'
#string = '拖延心理学【豆瓣拖延小组的镇组之宝】 (湛庐文化•心视界)'
#string = '明朝那些事儿(第1部):洪武大帝'
#string = '从一到无穷大（清华大学新生礼物，校长邱勇推荐！从一粒原子到无穷宇宙，一本书汇集人类认识世界、探索宇宙的方方面面） '
#string = '月亮与六便士(2019彩插新版，赠英文原版，“一本好书” 推荐。畅销100万册，完整无删减。荣登豆瓣年度高分榜)'
#r = r'(?<=【).*(?!=】)'
r = r'.(?<=\().*(?!=\))'
#r= r'(?<=（).*(?!=（)'
#r= r'(?<=（).*(?!=（)'



pattern = re.compile(r)
result0 = pattern.search(string)
if result0 is not None :
    print(result0)
    result = pattern.sub('',string)
    print(result)
#print(result.group(1))
#a = string.replace(result.group(1),'')
#print(a)



