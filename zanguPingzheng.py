'''
将税务系统的抵扣勾选增值税发票信息.xlsx导入到暂估冲线的模式凭证
'''

import pandas as pd
import os
import easygui


title = ['会计期间', '凭证类别字', '凭证类别排序号', '凭证编号', '行号', '制单日期', '附单据数', '制单人', '审核人',
       '记账人', '记账标志', '出纳人', '凭证标志', '凭证头自定义项1', '凭证头自定义项2', '摘要', '科目编码',
       '币种', '借方金额', '贷方金额', '外币借方金额', '外币贷方金额', '汇率', '数量借方', '数量贷方',
       '结算方式编码', '票号', '票号发生日期', '部门编码', '职员编码', '客户编码', '供应商编码', '项目编码',
       '项目大类编码', '业务员', '对方科目编码', '银行帐两清标志', '往来帐两清标志', '是否核销', '外部凭证帐套号',
       '外部凭证会计年度', '外部凭证系统名称', '外部凭证系统版本号', '外部凭证制单日期', '外部凭证会计期间', '外部凭证业务类型',
       '外部凭证业务号', '日期', '标志', '外部凭证单据号', '凭证是否可修改', '凭证分录是否可增删', '凭证合计金额是否保值',
       '分录数值是否可修改', '分录科目是否可修改', '分录受控科目可用状态', '分录往来项是否可修改', '分录部门是否可修改',
       '分录项目是否可修改', '分录往来项是否必输', '自定义字段1', '自定义字段2', '自定义字段3', '自定义字段4',
       '自定义字段5', '自定义字段6', '自定义字段7', '自定义字段8', '自定义字段9', '自定义字段10', '现金项目编号',
       '现金借方', '现金贷方']
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
zangu_pinzhen = pd.DataFrame(columns = title)
dic = dict(zip(title,range(len(title))))

zhidanriqi = easygui.enterbox('请输入制单日期"2024-3-18"')
qijian = int(zhidanriqi.split('-')[1])

msg = '请点选"抵扣勾选增值税发票信息.xlsx"'
fname_invoice = easygui.fileopenbox(msg)
path, file = os.path.split(fname_invoice)
os.chdir(path)
sheet_name = 'sheet1'
df_invoice = pd.read_excel(fname_invoice,sheet_name=sheet_name,dtype = {'金额*':'float64','票面税额*':'float64','有效抵扣税额*':'float64','购买方识别号*':str})
gongyingshangs2 = df_invoice['销售方纳税人名称']


msg = '请点选"供应商档案.xls"'
fname_gongyingshang = easygui.fileopenbox(msg)
df_gongyingshang = pd.read_excel(fname_gongyingshang,dtype={'供应商编码':str})
gongyingshangDic = dict(zip(df_gongyingshang['供应商名称'],df_gongyingshang['供应商编码']))
gongyings1 = df_gongyingshang['供应商名称']
gongyingshangs = set(gongyings1).intersection(set(gongyingshangs2))

df_invoice = df_invoice.loc[df_invoice['销售方纳税人名称'].isin(gongyingshangs)]
df_invoice = df_invoice.loc[~df_invoice['销售方纳税人名称'].isnull()]  # 删除记账为空的记录
last_xuhao = df_invoice.shape[0]
df_invoice.index = range(last_xuhao)

zangu_pinzhen['行号'] = list(range(last_xuhao*3))
for k, v in fixed_fields.items():
   zangu_pinzhen[k] = v

pingzhengbianhao = 0
for index, row in df_invoice.iterrows():
    xuhao = index * 3 + 1
    pingzhengbianhao = pingzhengbianhao + 1
    gongyingshang = row['销售方纳税人名称']
    buhansui = row['金额*']
    sui = row['有效抵扣税额*']
    sumary = '冲' + gongyingshang + '暂估'
    hansui = round(buhansui + sui, 2)
    print(gongyingshang, -1 * buhansui, sui, hansui)
    print('************')
    gongyingshang_bianma = gongyingshangDic.get(gongyingshang, '88888888')
    for i in range(3):
        if i == 0:
            zangu_pinzhen.iloc[xuhao - 1, dic['凭证编号']] = pingzhengbianhao
            zangu_pinzhen.iloc[xuhao - 1, dic['会计期间']] = qijian
            zangu_pinzhen.iloc[xuhao - 1, dic['制单日期']] = zhidanriqi
            zangu_pinzhen.iloc[xuhao - 1, dic['行号']] = 1
            zangu_pinzhen.iloc[xuhao - 1, dic['摘要']] = sumary
            zangu_pinzhen.iloc[xuhao - 1, dic['科目编码']] = '2271'
            zangu_pinzhen.iloc[xuhao - 1, dic['借方金额']] = 0
            zangu_pinzhen.iloc[xuhao - 1, dic['贷方金额']] = -1 * buhansui
            zangu_pinzhen.iloc[xuhao - 1, dic['供应商编码']] = '010010213'
            zangu_pinzhen.iloc[xuhao - 1, dic['对方科目编码']] = '2221001002'
            zangu_pinzhen.iloc[xuhao - 1, dic['票号发生日期']] = zhidanriqi
        elif i == 1:
            zangu_pinzhen.iloc[xuhao, dic['凭证编号']] = pingzhengbianhao
            zangu_pinzhen.iloc[xuhao, dic['会计期间']] = qijian
            zangu_pinzhen.iloc[xuhao, dic['制单日期']] = zhidanriqi
            zangu_pinzhen.iloc[xuhao, dic['行号']] = 2
            zangu_pinzhen.iloc[xuhao, dic['摘要']] = sumary
            zangu_pinzhen.iloc[xuhao, dic['科目编码']] = '2221001002'
            zangu_pinzhen.iloc[xuhao, dic['借方金额']] = sui
            zangu_pinzhen.iloc[xuhao, dic['贷方金额']] = 0
            zangu_pinzhen.iloc[xuhao, dic['供应商编码']] = ''
            zangu_pinzhen.iloc[xuhao, dic['对方科目编码']] = '2271'
            zangu_pinzhen.iloc[xuhao, dic['票号发生日期']] = zhidanriqi
        else:
            zangu_pinzhen.iloc[xuhao + 1, dic['凭证编号']] = pingzhengbianhao
            zangu_pinzhen.iloc[xuhao + 1, dic['会计期间']] = qijian
            zangu_pinzhen.iloc[xuhao + 1, dic['制单日期']] = zhidanriqi
            zangu_pinzhen.iloc[xuhao + 1, dic['行号']] = 3
            zangu_pinzhen.iloc[xuhao + 1, dic['摘要']] = sumary
            zangu_pinzhen.iloc[xuhao + 1, dic['科目编码']] = '2271'
            zangu_pinzhen.iloc[xuhao + 1, dic['借方金额']] = 0
            zangu_pinzhen.iloc[xuhao + 1, dic['贷方金额']] = hansui
            zangu_pinzhen.iloc[xuhao + 1, dic['供应商编码']] = gongyingshang_bianma
            zangu_pinzhen.iloc[xuhao + 1, dic['对方科目编码']] = '2221001002'
            zangu_pinzhen.iloc[xuhao + 1, dic['票号发生日期']] = zhidanriqi


zangu_pinzhen.to_excel('冲暂估模式凭证.xls',index = False)
os.startfile('冲暂估模式凭证.xls')


