'''
将工厂对销售公司的的销售订单进行汇总
将销售公司下面的三个机构对客户的销售订单进行汇总
对上面两个汇总进行对比，导出excel文件
'''


import pandas as pd
import numpy as np


#工厂的列标题
lst_columns = [
 '单据编号',
  '单据日期',
  '存货编码',
 '规格型号',
 '数量(本）',
 '数量2（件）',
  '金额']

#机构的列标题有点不一样
lst_columns_jigou = [
 '单据编号',
  '单据日期',
  '存货编码',
 '规格型号',
 '数量',
 '数量（件）',
  '金额']

def chuliXiaoshouDingdan(fname,lst_columns):
    df = pd.read_excel(fname)
    df = df[lst_columns]
    df = df.iloc[:-1]
    return df
 

#销售订单-工厂to销售公司
fname_gongchangToXiaoshou01 =  r"F:\a00nutstore\008\zw08\用友报价\产成品库存\销售订单-工厂to销售公司0726-0815.xlsx"
df_gongchangToXiaoshou01 = chuliXiaoshouDingdan(fname_gongchangToXiaoshou01,lst_columns)
fname_gongchangToXiaoshou02 =  r"F:\a00nutstore\008\zw08\用友报价\产成品库存\销售订单-工厂to销售公司0816-0825.xlsx"
df_gongchangToXiaoshou02 = chuliXiaoshouDingdan(fname_gongchangToXiaoshou02,lst_columns)
df_gongchangToXiaoshou = pd.concat([df_gongchangToXiaoshou01,df_gongchangToXiaoshou02])   #一次不能导出超过5000条的记录，分两次


##销售订单-佳广to客户
fname_jiaguang = r"F:\a00nutstore\008\zw08\用友报价\产成品库存\销售订单-佳广to客户0726-0825.xlsx"
df_jiaguang = chuliXiaoshouDingdan(fname_jiaguang,lst_columns_jigou)

##销售订单-荣佳to客户
fname_rongjia = r"F:\a00nutstore\008\zw08\用友报价\产成品库存\销售订单-荣佳to客户0726-0825.xlsx"
df_rongjia = chuliXiaoshouDingdan(fname_rongjia,lst_columns_jigou)

##销售订单-莱新to客户
fname_laixin01 = r"F:\a00nutstore\008\zw08\用友报价\产成品库存\销售订单统计表-莱新to客户0726-0815.xlsx"
df_laixin01 = chuliXiaoshouDingdan(fname_laixin01,lst_columns_jigou)
fname_laixin02 = r"F:\a00nutstore\008\zw08\用友报价\产成品库存\销售订单统计表-莱新to客户0816-0825.xlsx"  #一次不能导出超过5000条的记录，分两次
df_laixin02 = chuliXiaoshouDingdan(fname_laixin02,lst_columns_jigou)
df_laixin = pd.concat([df_laixin01,df_laixin02])
# 三个机构合并
df_jigou = pd.concat([df_laixin,df_jiaguang,df_rongjia])
df_jigou.head(5)

#机构数据透视表
pivot_jigou = pd.pivot_table(df_jigou,index = '存货编码',values =  ['数量','数量（件）','金额'],aggfunc = np.sum,fill_value = 0)

#工厂数据透视表
pivot_gongchang = pd.pivot_table(df_gongchangToXiaoshou,index = '存货编码',values =  ['数量(本）','数量2（件）','金额'],aggfunc = np.sum,fill_value = 0)

#两张透视表差异
pivot_diff = pd.merge(pivot_gongchang,pivot_jigou,left_index = True,right_index = True ,how = 'outer')


#添加差异列
pivot_diff['本数差异'] = pivot_diff['数量(本）'] - pivot_diff['数量']
pivot_diff['件数差异'] = pivot_diff['数量2（件）'] - pivot_diff['数量（件）']
pivot_diff['金额差异'] = pivot_diff['金额_x'] - pivot_diff['金额_y']

#差异存入excel文件中
pivot_diff.to_excel('工厂to销售公司vs各机构to客户202408.xlsx')

#工厂的销售订单
df_gongchangToXiaoshou.to_excel('工厂.xlsx',index = False)



