import pdfplumber
import re
import easygui
import os


def writeDangtian(fname):
    pdf = pdfplumber.open(fname)
    # print('开始读取数据')
    filename = 'pdf88.txt'
    with open(filename, 'w',encoding = 'utf-8') as f:
        f.write('')
    with open(filename, 'a',encoding = 'utf-8') as f:
        for page in pdf.pages:
            content = page.extract_text()
            f.write(content)
    pdf.close()
    return filename

def matchNumber(filename):
    regex = re.compile(r'CNY\s+(\d+\.\d{2})')
    regex1 = re.compile(r'Grand Total\s+((\d+,\d{3}\.\d{2})|(\d{2,3}\.\d{2}))')
    regex2 = re.compile(r'Holiday Inn Riverside Wuhan\s+(?P<day>\d{1,2})\-(?P<month>\d{1,2})\-(?P<year>\d{1,4}$)')
    numbers = []
    hejishu = 0
    riqi = '2010 年1月12日'
    with open(filename, 'r') as f:
        for hang in f.readlines():
            mat = regex.search(hang)
            mat1 = regex1.search(hang)
            mat2 = regex2.search(hang)
            if mat2 :
                year = mat2.group('year')
                month = mat2.group('month')
                day = mat2.group('day')
                riqi = '20'+year+'年' +month+'月'+day+'日'
            elif mat:
                numbers.append(mat.group(1))
            elif mat1:
                hejishu = mat1.group(1)
            else:
                continue
    numbers = [float(j) for j in numbers]
    return numbers, hejishu,riqi

def countGeshu(numbers, hejishu,riqi,newprices):
    renshufilename = 'renshu.txt'
    danjias = [25.73,44.18,12.86,25.72,30.02,34.31,38.59]
    if newprices == []:
        danjias = danjias
    else :
        for newprice in newprices:
            if newprice not in danjias :
                danjias.append(newprice)
    for danjia in danjias:
        danjia = 0
    danjia_dic1 = {danjia:numbers.count(danjia) for danjia in danjias}
    geshus = []
    for danjia in danjias:
        geshu = 0
        for number in numbers:
            if number not in danjias:
                if int(100*number)%int(100*danjia) <=0.001:
                    geshu = geshu + number/danjia
        geshus.append(geshu)
    danjia_dic2 = dict(zip(danjias,geshus))
    danjia_dic = {}
    for danjia,geshu in danjia_dic1.items():
        danjia_dic[danjia] = geshu + danjia_dic2.get(danjia,0)
    heji= float(hejishu.replace(',',''))
    jisuan_jiner = 0
    for key,value in danjia_dic.items():
        jisuan_jiner+=key*value
    if round(jisuan_jiner, 2) == heji:
        with open('renshu.txt', 'w',encoding = 'utf-8') as f:
            f.write('计算正确\n')
            f.write('日期: {}\n'.format(riqi))
            f.write('总金额是{}元\n'.format(heji))
            for key,value in danjia_dic.items():
                if value != 0 :
                    f.write('{}有{}个\n'.format(key,int(value)))
            f.write('总人数有{}人\n'.format(int(sum(danjia_dic.values()))))
    else:
        with open('renshu.txt', 'w',encoding = 'utf-8') as f:
            f.write('计算有误，请注意有新情况发生！\n')
            f.write('日期: {}\n'.format(riqi))
            f.write('总金额是{}元\n'.format(heji))
            for key, value in danjia_dic.items():
                if value != 0:
                    f.write('{}有{}个\n'.format(key, int(value)))
            f.write('总人数有{}人\n'.format(int(sum(danjia_dic.values()))))
    for key,value in danjia_dic.items():
        if value != 0 :
             print('{}有{}个'.format(key,int(value)))
    print('总人数有{}人'.format(int(sum(danjia_dic.values()))))
    os.system(renshufilename)
    return renshufilename

def res_path(relative_path):
    """获取资源绝对路径"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def main():
    msg = '请点选OperaPrint.pdf文件'
    print(msg)
    res_path('img/ucrtbase.dll')
    fname = easygui.fileopenbox(msg)
    filename = writeDangtian(fname)
    numbers, hejishu,riqi = matchNumber(filename)
    print(('总金额是{}元\n'.format(hejishu)))
    msg = '是否有新早餐单价？'
    print(msg)
    choice = easygui.ccbox(msg,title='请选择Yes or No',choices=('Yes','No'))
    if choice == False :
        newprices = []
    else :
        msg = '请输入新的早餐单价'
        print(msg)
        newprices = easygui.multenterbox(msg,fields = ['早餐单价{}'.format(j) for j in range(1,7)])
        newprices = [float(newprice) for newprice in newprices if newprice not in [None,'' ]]
    renshufilename = countGeshu(numbers, hejishu,riqi,newprices)

if __name__ == '__main__':
    main()


