
'''
根据五家新公司、双佳003、莱特及大凭证上的成本，自动生成合并利润表当月数
根据选取的上月数，计算出合并利润表的累计数
'''
import pandas as pd
import os
import easygui
import re
import openpyxl


#五家新公司利润表统一格式
dic = {'一、产品销售收入': '一、营业收入',
 '减：销售成本': '减：营业成本',
 '销售税金及附加': '营业税金及附加',
 '减：销售费用': '减：销售费用',
 '管理费用': '管理费用',
 '财务费用': '财务费用',
 '营业外收入': '加：营业外收入',
 '其它': '投资收益（损失以"-"填列）',
 '减：营业外支出': '减：营业外支出'}




# fname_xiaoshou = r"F:\a00nutstore\008\zw08\新公司\7月财务报表\湖北双佳纸业销售有限公司利润表7月新.xls"
def getShouruChenben(fname):
    df = pd.read_excel(fname,header = 3)
    df.columns = ['xiangmu','benyue','leiji']
    df = df.fillna(0)
    df['xiangmu']= df['xiangmu'].str.strip()
    df = df.set_index('xiangmu')
    shouru = df.loc['一、营业收入','benyue']
    chenben = df.loc['减：营业成本','benyue']
    return df,shouru,chenben
    
fname_laite = r"F:\a00nutstore\008\zw08\新公司\7月财务报表\莱特202407利润表.csv"
def getLaite(fname_laite):
    df_laite = pd.read_csv(fname_laite,encoding = 'GBK')  #dtype = {'C本 月 数':'float64','D本年累计数':'float64'}
    df_laite = df_laite.fillna(0)
    df_laite.drop('B行次',inplace = True,axis = 1)
    df_laite.columns = ['xiangmu','benyue','leiji']
    df_laite.xiangmu = df_laite.xiangmu.str.strip()
    df_laite = df_laite.set_index('xiangmu')
    df_laite.benyue = df_laite.benyue.str.replace(',','')
    df_laite.benyue = df_laite.benyue.astype('float64')
    df_laite.leiji = df_laite.leiji.str.replace(',','')
    df_laite.leiji = df_laite.leiji.astype('float64')
    shouru = df_laite.loc['一，产品销售收入','benyue']
    qitalirun = df_laite.loc['加：其他业务利润','benyue']
    df_laite.loc['一，产品销售收入','benyue'] = shouru + qitalirun
    df_laite.index = df_laite.index.map({'一，产品销售收入': '一、营业收入',
     '减：产品销售成本': '减：营业成本',
     '产品销售税金及附加': '营业税金及附加',
     '产品销售费用': '销售费用',
     '减：管理费用': '管理费用',
     '财务费用': '财务费用',
     '加：投资收益': '投资收益（损失以"-"填列）',
     '三，营业利润': '二、营业利润（亏损以"－"号填列）',
     '营业外收入': '加：营业外收入',
     '减：营业外支出': '减：营业外支出',
     '四，利润总额': '三、利润总额（亏损总额以"－"号填列）',
     '减：所得税': '减：所得税费用',
     '五，净利润': '四、净利润（净亏损以"－"号填列）'})
    
    df_laite = df_laite.loc[df_laite.index.dropna()]
    df_laite =  df_laite.loc[ ['一、营业收入',
     '减：营业成本',
     '营业税金及附加',
     '销售费用',
     '管理费用',
     '财务费用',
     '投资收益（损失以"-"填列）',
     '二、营业利润（亏损以"－"号填列）',
     '加：营业外收入',
     '减：营业外支出',
     '三、利润总额（亏损总额以"－"号填列）',
     '减：所得税费用',
     '四、净利润（净亏损以"－"号填列）']]
    df_laite= df_laite.reindex(index =['一、营业收入',
     '减：营业成本',
     '营业税金及附加',
     '销售费用',
     '管理费用',
     '财务费用',
     '资产减值损失',
     '加：公允价值变动收益（损失以"-"填列）',
     '投资收益（损失以"-"填列）',
     '其中：对联营企业和合营企业的投资收益',
     '二、营业利润（亏损以"－"号填列）',
     '加：营业外收入',
     '减：营业外支出',
     '其中：非流动资产处置损失',
     '三、利润总额（亏损总额以"－"号填列）',
     '减：所得税费用',
     '四、净利润（净亏损以"－"号填列）',
     '五、每股收益：',
     '（一）基本每股收益',
     '（二）稀释每股收益']
    ,fill_value = 0)
    shouru = df_laite.loc['一、营业收入','benyue']
    chenben = df_laite.loc['减：营业成本','benyue']
    return df_laite,shouru,chenben


path = r'F:\a00nutstore\008\zw08\新公司\7月财务报表'
os.chdir(path)
lirunLst = [i for i in os.listdir(path) if ('利润' in i) and (not i.startswith('~$')) ]
lirunLst


# for i in ['双佳','莱特','销售','莱新','佳广','荣佳','佳科']:
#销售收入抵减
jian_shouru = []
#销售成本抵减
jian_chengben = []
data = []
for file in lirunLst:
    if ('莱特' in file) and (file.endswith('.csv')):
        # fname_laite = r"F:\a00nutstore\008\zw08\新公司\7月财务报表\莱特202407利润表.csv"
        df_laite,shouru,chenben= getLaite(fname_laite)
        data.append(df_laite)
        jian_shouru.append(chengben)
        jian_chengben.append(chengben)
    else :
        
        if  ('双佳' in file) and ('销售' not in file):
            df,shouru,chengben = getShouruChenben(os.path.join(path,file))
            data.append(df)
            # jian_shouru.append(chengben)
            # jian_chengben.append(chengben)
            
        elif  '销售' in file:
            df,shouru,chengben = getShouruChenben(os.path.join(path,file))
            data.append(df)
            jian_shouru.append(chengben)
            jian_chengben.append(chengben)
        elif '莱新' in file:
            df,shouru,chengben = getShouruChenben(os.path.join(path,file))
            data.append(df)
            jian_shouru.append(chengben)
            jian_chengben.append(chengben)
        elif '佳广' in file:
            df,shouru,chengben = getShouruChenben(os.path.join(path,file))
            data.append(df)
            jian_shouru.append(chengben)
            jian_chengben.append(chengben)
        elif '荣佳' in file:
            df,shouru,chengben = getShouruChenben(os.path.join(path,file))
            data.append(df)
            jian_shouru.append(chengben)
            jian_chengben.append(chengben)
        elif '佳科' in file:
            df,shouru,chengben = getShouruChenben(os.path.join(path,file))
            data.append(df)
            jian_shouru.append(chengben)
            jian_chengben.append(chengben)
        else :
            continue

    
        
    


# In[11]:


result0 = pd.concat(data)
benyue = result0.groupby('xiangmu',sort = False)['benyue'].sum()
leiji = result0.groupby('xiangmu',sort = False)['leiji'].sum()
result = pd.DataFrame({'benyue':benyue,'leiji':leiji},columns = ['benyue','leiji'])
result


# In[12]:


result.loc['一、营业收入','benyue'] = result.loc['一、营业收入','benyue'] - sum(jian_shouru)
result.loc['减：营业成本'] = result.loc['减：营业成本','benyue'] -  sum(jian_chengben)
result.loc['二、营业利润（亏损以"－"号填列）','benyue'] = result.loc['二、营业利润（亏损以"－"号填列）','benyue'] - sum(jian_shouru) + sum(jian_chengben)
result.loc['二、营业利润（亏损以"－"号填列）','leiji'] = result.loc['二、营业利润（亏损以"－"号填列）','bleiji'] - sum(jian_shouru) + sum(jian_chengben)


# In[13]:


result


# In[15]:


result.to_excel('2222.xlsx')


# In[7]:


sum(jian_chengben)


# In[8]:


sum(jian_shouru)


# In[ ]:





# In[ ]:


fname_laite = r"F:\a00nutstore\008\zw08\新公司\7月财务报表\莱特202407利润表.csv"
def getLaite(fname_laite):
    df_laite = pd.read_csv(fname_laite,encoding = 'GBK')  #dtype = {'C本 月 数':'float64','D本年累计数':'float64'}
    df_laite.drop('B行次',inplace = True,axis = 1)
    df_laite.columns = ['xiangmu','benyue','leiji']
    df_laite.xiangmu = df_laite.xiangmu.str.strip()
    df_laite = df_laite.set_index('xiangmu')
    df_laite.benyue = df_laite.benyue.str.replace(',','')
    df_laite.benyue = df_laite.benyue.astype('float64')
    shouru = df_laite.loc['一，产品销售收入','benyue']
    qitalirun = df_laite.loc['加：其他业务利润','benyue']
    df_laite.loc['一，产品销售收入','benyue'] = shouru + qitalirun
    df_laite.index = df_laite.index.map({'一，产品销售收入': '一、营业收入',
     '减：产品销售成本': '减：营业成本',
     '产品销售税金及附加': '营业税金及附加',
     '产品销售费用': '销售费用',
     '减：管理费用': '管理费用',
     '财务费用': '财务费用',
     '加：投资收益': '投资收益（损失以"-"填列）',
     '三，营业利润': '二、营业利润（亏损以"－"号填列）',
     '营业外收入': '加：营业外收入',
     '减：营业外支出': '减：营业外支出',
     '四，利润总额': '三、利润总额（亏损总额以"－"号填列）',
     '减：所得税': '减：所得税费用',
     '五，净利润': '四、净利润（净亏损以"－"号填列）'})
    
    df_laite = df_laite.loc[df_laite.index.dropna()]
    df_laite =  df_laite.loc[ ['一、营业收入',
     '减：营业成本',
     '营业税金及附加',
     '销售费用',
     '管理费用',
     '财务费用',
     '投资收益（损失以"-"填列）',
     '二、营业利润（亏损以"－"号填列）',
     '加：营业外收入',
     '减：营业外支出',
     '三、利润总额（亏损总额以"－"号填列）',
     '减：所得税费用',
     '四、净利润（净亏损以"－"号填列）']]
    df_laite= df_laite.reindex(index =['一、营业收入',
     '减：营业成本',
     '营业税金及附加',
     '销售费用',
     '管理费用',
     '财务费用',
     '资产减值损失',
     '加：公允价值变动收益（损失以"-"填列）',
     '投资收益（损失以"-"填列）',
     '其中：对联营企业和合营企业的投资收益',
     '二、营业利润（亏损以"－"号填列）',
     '加：营业外收入',
     '减：营业外支出',
     '其中：非流动资产处置损失',
     '三、利润总额（亏损总额以"－"号填列）',
     '减：所得税费用',
     '四、净利润（净亏损以"－"号填列）',
     '五、每股收益：',
     '（一）基本每股收益',
     '（二）稀释每股收益']
    ,fill_value = 0)
    shouru = df_laite.loc['一、营业收入','benyue']
    chenben = df_laite.loc['减：营业成本','benyue']
    return shouru,chenben,df_laite
shouru,chenben,df_laite = getLaite(fname_laite)
df_laite


# In[ ]:


'202407佳广利润表.xls'.startswith('.xlsx')


# In[ ]:


'202407佳广利润表.xls'.endswith('.xlsx')


# In[ ]:


print(shouru,chenben)


# In[ ]:




