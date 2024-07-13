'''
将当月工资表上扣社保明细与公司缴纳社保明细进行对比，发现差异，生成下面两个名单：
1. 工资已扣社保而公司未缴社保人员名单
2. 公司已缴社保而工资表上未扣人员名单

'''
import easygui
import pandas as pd
import os
import re

#生产工资
def shengcan(msg):
    fname = easygui.fileopenbox(msg)
    path,filename = os.path.split(fname)
    os.chdir(path)
    sheet_name = '工资'
    df= pd.read_excel(fname,sheet_name = sheet_name)
    df = df.loc[:,['车间','卡号','姓名','代扣社保']]
    df.columns = ['部门车间','卡号','姓名','社保']
    df = df.loc[df['社保'].notna()]
    df = df.loc[df['社保']==383]
    return df

#行管工资
def xingguan(msg):
    fname = easygui.fileopenbox(msg)
    sheet_name = '工资'
    df = pd.read_excel(fname, sheet_name=sheet_name)
    df = df[df['公司'] == '双佳']
    df = df.loc[:, ['部门', '账号', '姓名', '社保']]
    df.columns = ['部门车间', '卡号', '姓名', '社保']
    df = df.loc[df['社保'].notna()]
    return df

def choiceSheetname(df):
    sheet_names = [key for key in df.keys() ]
    if len(sheet_names) == 1:
        sheet_name = sheet_names[0]
    else :
        sheet_name = easygui.choicebox(msg = '请点选工作表',choices = sheet_names)
    return sheet_name

def shebao():
    msg = '请选择"养老保险明细"excel文件'
    fname = easygui.fileopenbox(msg)
    df = pd.read_excel(fname, sheet_name=None)
    sheet_name = choiceSheetname(df)
    df = pd.read_excel(fname,sheet_name = sheet_name)
    df = df.loc[:, ['社会保障号码', '姓名', '个人合计']]
    return df

def main():
    df_shengcan = shengcan('请选择生产人员工资"excel文件')
    df_xingguan = xingguan('请选择行管人员工资"excel文件')
    df_chebao = shebao()
    df_gongzi = pd.concat([df_shengcan, df_xingguan])
    df8 = pd.merge(df_gongzi, df_chebao, how='outer', on=['姓名'])
    #工资已扣社保而公司未缴
    df_gongzi_chebao = df8.loc[df8['社保'].notna() & df8['个人合计'].isnull()]
    df_gongzi_chebao.index = range(1, len(df_gongzi_chebao) + 1)
    df_gongzi_chebao = df_gongzi_chebao.iloc[:, :3]
    df_gongzi_chebao.insert(0, '序号', value=df_gongzi_chebao.index)
    df_gongzi_chebao.to_excel('工资已扣社保而公司未缴社保人员名单.xlsx',index = False)
    #公司已缴社保而工资表上未扣
    df_chebao_gongzi = df8.loc[df8['社保'].isnull() & df8['个人合计'].notna()]
    df_chebao_gongzi.index = range(1, len(df_chebao_gongzi) + 1)
    df_chebao_gongzi = df_chebao_gongzi.iloc[:, :3]
    df_chebao_gongzi.insert(0, '序号', value=df_chebao_gongzi.index)
    df_chebao_gongzi.to_excel('公司已缴社保而工资表上未扣人员名单.xlsx',index = False)

    os.startfile('工资已扣社保而公司未缴社保人员名单.xlsx')
    os.startfile('公司已缴社保而工资表上未扣人员名单.xlsx')


if __name__ == '__main__':
    main()
