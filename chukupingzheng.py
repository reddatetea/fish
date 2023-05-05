#原材料出库凭证模板生成脚本
#凭证导入导出完整：路径C:\UFSMART\T3系统工具\Excel\导入导出文件.凭证.xls
#引入引出凭证入口：T3系列管理软件\T3\T3系列工具\数据导入导出

import pandas as pd
import xlwings as xw
import easygui
import os

msg = '请点选原材料出库文件"原材料出库2022-07.xlsx"'
fname1 = easygui.fileopenbox(msg)
zhidanriqi = easygui.enterbox('请输入制单日期"2022-8-18"')
df1 = pd.read_excel(fname1)
path, file = os.path.split(fname1)
qijian = int(file.split('.')[0].split('-')[-1])
df2 = df1.loc[df1['科目名称'] != '合计']

title = ['会计期间',
         '凭证类别字',
         '凭证类别排序号',
         '凭证编号',
         '行号',
         '制单日期',
         '附单据数',
         '制单人',
         '审核人',
         '记账人',
         '记账标志',
         '出纳人',
         '凭证标志',
         '凭证头自定义项1',
         '凭证头自定义项2',
         '摘要',
         '科目编码',
         '币种',
         '借方金额',
         '贷方金额',
         '外币借方金额',
         '外币贷方金额',
         '汇率',
         '数量借方',
         '数量贷方',
         '结算方式编码',
         '票号',
         '票号发生日期',
         '部门编码',
         '职员编码',
         '客户编码',
         '供应商编码',
         '项目编码',
         '项目大类编码',
         '业务员',
         '对方科目编码',
         '银行帐两清标志',
         '往来帐两清标志',
         '是否核销',
         '外部凭证帐套号',
         '外部凭证会计年度',
         '外部凭证系统名称',
         '外部凭证系统版本号',
         '外部凭证制单日期',
         '外部凭证会计期间',
         '外部凭证业务类型',
         '外部凭证业务号',
         '日期',
         '标志',
         '外部凭证单据号',
         '凭证是否可修改',
         '凭证分录是否可增删',
         '凭证合计金额是否保值',
         '分录数值是否可修改',
         '分录科目是否可修改',
         '分录受控科目可用状态',
         '分录往来项是否可修改',
         '分录部门是否可修改',
         '分录项目是否可修改',
         '分录往来项是否必输',
         '自定义字段1',
         '自定义字段2',
         '自定义字段3',
         '自定义字段4',
         '自定义字段5',
         '自定义字段6',
         '自定义字段7',
         '自定义字段8',
         '自定义字段9',
         '自定义字段10',
         '现金项目编号',
         '现金借方',
         '现金贷方']
fixed_fields = {'凭证类别字': '记',
                '凭证类别排序号': 1,
                '附单据数': -1,
                '制单人': '张文伟',
                '数量借方': 0,
                '是否核销': 0,
                '外部凭证单据号': 0,
                '凭证是否可修改': 1,
                '凭证分录是否可增删': 0,
                '凭证合计金额是否保值': 0,
                '分录数值是否可修改': 1,
                '分录科目是否可修改': 1,
                '分录受控科目可用状态': 1,
                '分录往来项是否可修改': 1,
                '分录部门是否可修改': 1,
                '分录项目是否可修改': 1,
                '分录往来项是否必输': 0
                }


dic = {'纸  小计': '5001002',
       '灰板  小计': '5001003',
       '辅料  小计': '5001004',
       '包装物  小计': '5001006'}


hanghao = len(df2)
df_pinzhen = pd.DataFrame(columns=title)
df_pinzhen['行号'] = range(1, hanghao + 1)
df_pinzhen['会计期间'] = qijian
df_pinzhen['制单日期'] = zhidanriqi
df_pinzhen['摘要'] = '原材料出库{}'.format(str(qijian))

for k, v in fixed_fields.items():
   df_pinzhen[k] = v


def func(dic, s):
    s1 = []
    for i in s:
        j = dic.get(i.strip(), i)
        s1.append(j)
    return s1

kemubianma = func(dic, df2['科目编码'].to_list())
df_pinzhen['科目编码'] = kemubianma

def jiner(kemu, jiner):
    jie = []
    dai = []
    for kemu, i in zip(kemu, jiner):
        if '计' in kemu:
            jie.append(i)
            dai.append(0)
        else:
            dai.append(i)
            jie.append(0)
    return jie, dai

jie, dai = jiner(df2['科目编码'], df2['金额'])
df_pinzhen['借方金额'] = jie
df_pinzhen['贷方金额'] = dai
df_pinzhen['数量贷方'] = df2['出库'].to_list()
df_pinzhen['数量贷方'] = df_pinzhen['数量贷方'].fillna(0)
fname_pingzheng = os.path.join(path,'凭证{}.xls'.format(str(qijian)))
df_pinzhen.to_excel(fname_pingzheng,'Sheet1', index=False)
os.startfile(fname_pingzheng)




