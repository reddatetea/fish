'''
将食堂消费明细与当月工资表上的人员进行对比，发现食堂打卡异常情况，形成"食堂打卡明细.xlsx"和‘食堂打卡明细.xlsx'两个文件
'''

import os
import numpy as np
import pandas as pd
import easygui

def choiceSheetname(df):
    sheet_names = [key for key in df.keys() ]
    if len(sheet_names) == 1:
        sheet_name = sheet_names[0]
    else :
        sheet_name = easygui.choicebox(msg = '请点选工作表',choices = sheet_names)
    return sheet_name
def shitang():
    columns = ['工号', '卡号', '姓名', '部门名称', '机号', '卡流水号', '消费时间']
    # fname_shitang = r"F:\a00nutstore\008\zw08\食堂\消费数据明细2024.1.1-2024.4.18可编辑.xlsx"
    msg = '请选择食堂"消费数据明细"excel文件'
    fname_shitang = easygui.fileopenbox(msg)
    path, filename = os.path.split(fname_shitang)
    os.chdir(path)
    df = pd.read_excel(fname_shitang, sheet_name = None)
    sheet_name = choiceSheetname(df)
    df_shitang = pd.read_excel(fname_shitang, sheet_name = sheet_name,usecols=columns,
                               dtype={'卡号': 'str', '工号': 'str', '机号': 'str', '消费时间': 'datetime64[ns]'})
    df_shitang['year'] = df_shitang['消费时间'].dt.year
    df_shitang['month'] = df_shitang['消费时间'].dt.month
    df_shitang['day'] = df_shitang['消费时间'].dt.day
    df_shitang['hour'] = df_shitang['消费时间'].dt.hour
    df_shitang['minute'] = df_shitang['消费时间'].dt.minute
    df_shitang['second'] = df_shitang['消费时间'].dt.second
    df_shitang = df_shitang.assign(year=df_shitang.year.apply(lambda x: zfillSer(x, 4)))
    df_shitang = df_shitang.assign(month=df_shitang.month.apply(lambda x: zfillSer(x, 2)))
    df_shitang = df_shitang.assign(day=df_shitang.day.apply(lambda x: zfillSer(x, 2)))
    df_shitang = df_shitang.assign(minute=df_shitang.minute.apply(lambda x: zfillSer(x, 2)))
    df_shitang = df_shitang.assign(second=df_shitang.second.apply(lambda x: zfillSer(x, 2)))
    df_shitang['qijian'] = df_shitang['year'] + '-' + df_shitang['month']
    df_shitang = df_shitang.assign(yongcan=df_shitang.hour.agg(zhaoZhongWan))
    # 删除重复打卡
    df_shitang = df_shitang.drop_duplicates(
        subset=['工号', '卡号', '姓名', '部门名称', '机号', 'year', 'month', 'day', 'yongcan'], keep='first')

    # 字典
    shitang_names = df_shitang['姓名'].to_list()
    shitang_bumen = df_shitang['部门名称'].to_list()
    shitang_time = df_shitang['消费时间'].to_list()
    shitang_gonghao = df_shitang['工号'].to_list()
    shitang_kahao = df_shitang['卡号'].to_list()
    shitang_qijian = df_shitang['qijian'].to_list()
    shitang_whichCan = df_shitang['yongcan'].to_list()
    dic_shitang = dict(zip(shitang_names,
                           zip(shitang_gonghao, shitang_kahao, shitang_bumen, shitang_time, shitang_qijian,
                               shitang_whichCan)))
    return df_shitang,shitang_names,dic_shitang


#填充月份、天、小时、分钟和秒至两位数并转为字符型
def zfillSer(ser,number):
    ser = str(ser).zfill(number)
    return ser

#根据打卡时间，确定是早餐、中餐还是晚餐
def zhaoZhongWan(ser):
    if int(ser) < 10:
        return '早餐'
    elif 10 <= int(ser) <= 16:
        return '中餐'
    else:
        return '晚餐'

#提取生产人员工资表中的当月人名
def shengcan():
    msg = '请选择"生产人员工资"excel文件'
    fname_shengcan = easygui.fileopenbox(msg)
    sheet_name = '工资'
    df_shengcan = pd.read_excel(fname_shengcan,sheet_name = sheet_name)
    shengcan_names = df_shengcan['姓名'].to_list()
    return shengcan_names

#提取行管工资表中的当月人名
def laowu():
    msg = '请选择"劳务工资"excel文件'
    fname_laowu = easygui.fileopenbox(msg)
    df_laowu = pd.read_excel(fname_laowu,sheet_name = '工资')
    laowu_names = df_laowu['姓名'].to_list()
    return laowu_names

def xingguan():
    msg = '请选择"实时工资"excel文件'   #行管人员工资
    fname_xingguan = easygui.fileopenbox(msg)
    sheet_name = '工资'
    df_xingguan = pd.read_excel(fname_xingguan,sheet_name = sheet_name)
    xingguan_names = df_xingguan['姓名'].to_list()
    return xingguan_names

#提取劳务派遣工资表中的当月人名

def main():
    #食堂卡更名文件
    right = pd.read_excel(r"F:\a00nutstore\008\zw08\食堂\食堂卡需要更名的名单.xlsx",'需要更名',dtype = {'卡号':'str','工号':'str','机号':'str','消费时间':'datetime64[ns]'})
    df_shitang, shitang_names, dic_shitang = shitang()
    df_shitang.to_excel('食堂打卡明细.xlsx', index=False)
    shengcan_names = shengcan()
    xingguan_names = xingguan()
    laowu_names = laowu()
    error_names = list(set(shitang_names) - set(xingguan_names + shengcan_names + laowu_names))
    # 根据异常人员名单和食堂人员字典，形成食常卡异常明细
    data = []
    for name in list(error_names):
        kahao = dic_shitang[name][0]
        gonghao = dic_shitang[name][1]
        bumen = dic_shitang[name][2]
        time = dic_shitang[name][3]
        qijian = dic_shitang[name][4]
        zhaozhongwan = dic_shitang[name][5]
        data0 = [kahao, gonghao, name, bumen, time, qijian, zhaozhongwan]
        data.append(data0)
    left = pd.DataFrame(data, columns=['工号', '卡号', '姓名', '部门名称', '最后打卡时间', '期间', '用餐'])
    left = left.sort_values(['工号', '卡号'])
    # 更正食堂卡上错误的姓名
    df_left_right = pd.merge(left,right,how = 'left',on = ['工号', '卡号', '姓名', '部门名称'])
    df_left_right['姓名'] = np.where(df_left_right['异常原因'].notna(), df_left_right['异常原因'],
                            df_left_right['姓名'])
    df_left_right = df_left_right.loc[~df_left_right['异常原因'].notna()]
    df_left_right.to_excel('食堂打卡异常.xlsx', index=False)
    os.startfile('食堂打卡明细.xlsx')
    os.startfile('食堂打卡异常.xlsx')


if __name__ == '__main__':
    main()

