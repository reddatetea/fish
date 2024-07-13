import easygui
import os
import pandas as pd

dtype = {'商品id': str, '样式ID': str}
choices = ['单文件', '文件夹']
skiprows = 0


def CsvToNumber(fname, skiprows):
    os.chmod(fname, 0o777)

    path, suffix = os.path.splitext(fname)
    _, file = os.path.split(fname)
    fname_xlsx = ''.join([path, '正.xlsx'])
    if suffix.lower() == '.csv':
        df = pd.read_csv(fname, dtype=dtype, skiprows=skiprows)
        df.to_excel(fname_xlsx, index=False)
        os.startfile(fname_xlsx)
    elif suffix.lower() in ['.xlsx', '.xls']:
        df = pd.read_excel(fname, dtype=dtype, skiprows=skiprows)
        df.to_excel(fname_xlsx, index=False)
        os.startfile(fname_xlsx)
    else:
        pass


choice = easygui.choicebox(msg='请选择处理模式', choices=choices)
if choice == '单文件':
    fname = easygui.fileopenbox(msg='请点选要处理的csv文件或excel文件')
    _, file = os.path.split(fname)
    try:
        CsvToNumber(fname, skiprows=skiprows)
    except:
        skiprows = easygui.enterbox('请输入数据开始于第几行', title='注意:数据行从列标题开始计算')
        skiprows = int(skiprows) - 1
        try:
            CsvToNumber(fname, skiprows=skiprows)
        except:
            easygui.msgbox(msg=f'{file}文件格式有误,不处理')



else:
    folder = easygui.diropenbox(msg='请点选文件夹', title='处理csv文件或excel文件')
    files = os.listdir(folder)
    for file in files:
        fname = os.path.join(folder, file)
        try:
            CsvToNumber(fname, skiprows=skiprows)
        except:
            continue


