#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
tcloud中用销售订单生成税局发票模板
'''
import os
import re
import easygui
import openpyxl
import numpy as np
import pandas as pd


# In[2]:


def danjuChuli(df):
    df = df.dropna(how='all', axis=0)
    cols = [i for i in df.columns.to_list() if 'Unnamed' not in i]
    df = df[cols]
    # get maxrows
    for label, ser in df.items():
        for num, x in enumerate(ser):
            if isinstance(x, str):
                if '合计' in x:
                    index = num
                    print(index)
                    break
    df = df.iloc[:index]
    df = df.dropna(how='all', axis=1)
    return df
def chuliMingchen(d):
    d['存货名称'] = d['存货名称'].str.replace('运费',"")
    qian = d['存货名称'].str.split('型').str[0]
    hou = d['存货名称'].str.split('型').str[1]
    qian = pd.Series(qian).fillna('')
    hou = pd.Series(hou).fillna('')
    return qian,hou


# In[3]:


#读取发票模板
fname_fapiao = r"F:\repos\fish\发票模板.xlsx"
df_fapiao = pd.read_excel(fname_fapiao,header = 2,dtype = {'商品和服务税收分类编码':'str'})
df_fapiao


# In[5]:


fname_dingdan = r"F:\repos\fish\肥猫销售订单SO-2024-04-0082.xlsx"
df_dingdan = pd.read_excel(fname_dingdan,sheet_name = 0,header = 8)
df_dingdan


# In[6]:


df_dingdan1 = danjuChuli(df_dingdan) 
qian,hou = chuliMingchen(df_dingdan1)
df_dingdan1


# In[ ]:


df_fapiao.columns.to_list()


# In[7]:


df_dingdan1['项目名称'] = df_dingdan1['货号'] + '-' + hou
df_dingdan1['项目名称'] = df_dingdan1['项目名称'].str.replace('运费-','运费')
df_dingdan1['商品和服务税收分类编码'] = '1060202010000000000'
df_dingdan1['规格型号'] = qian
df_dingdan1['单位'] = '本'
df_dingdan1['商品数量'] = df_dingdan1['数量（本）']
df_dingdan1['商品单价'] = df_dingdan1['单价']
df_dingdan1['金额'] = df_dingdan1['金额（元）']
df_dingdan1['税率'] = 0.01
df_dingdan1['折扣金额'] = ''
df_dingdan1['优惠政策类型'] = ''

df_dingdan2 = df_dingdan1[['项目名称',
 '商品和服务税收分类编码',
 '规格型号',
 '单位',
 '商品数量',
 '商品单价',
 '金额',
 '税率',
 '折扣金额',
 '优惠政策类型']]
df_dingdan2


# In[8]:


fname_result = r"F:\repos\fish\发票模板 - 副本.xlsx"

with pd.ExcelWriter(fname_result, engine='openpyxl',mode='a', if_sheet_exists='overlay')  as writer:
  
    df_dingdan2.to_excel(writer, sheet_name = '1-明细模板',startrow=3, header = False,index = False)






# In[ ]:


#提取发票台头等
fname_taitou = r"F:\repos\fish\肥猫销售订单SO-2024-04-0082.xlsx"
df_taitou = pd.read_excel(fname_dingdan,sheet_name = 0)
df_taitou1 = df_taitou.iloc[:,[1,3]]
df_taitou1.columns = ['kehu','names' ]
for i,j in zip(df_taitou1['kehu'],df_taitou1['names']):
    if i == '发货单号：':
        danhao = j
    elif i == '客户名称：':
        kehu = j
    else:
        continue
print(danhao,kehu)

