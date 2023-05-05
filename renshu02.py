import pdfplumber
import re
import easygui
import time
import os

def writeDangtian(fname):

    pdf = pdfplumber.open(fname)
    #print('开始读取数据')
    filename = 'pdf88.txt'
    with open(filename,'w') as f:
        f.write('')
    with open(filename,'a') as f:
        for page in pdf.pages:
            content = page.extract_text()
            #print(content)
            f.write(content)

    pdf.close()
    #print('保存成功！')
    return filename


def matchNumber(filename):
    regex = re.compile(r'CNY\s+(\d+\.\d{2})')
    regex1 =  re.compile(r'Grand Total\s+((\d+,\d{3}\.\d{2})|(\d{2,3}\.\d{2}))')
    numbers = []
    hejishu = 0
    with open(filename, 'r') as f:
        for hang in f.readlines():
            #print(hang)
            mat = regex.search(hang)

            if mat :

                numbers.append(mat.group(1))
            else :
                continue

    with open(filename, 'r') as f:
        for hang in f.readlines():
            mat1 = regex1.search(hang)
            if mat1 :
                hejishu = mat1.group(1)
            else :
                continue


    return numbers,hejishu

def countGeshu(numbers,hejishu):
    renshufilename = 'renshu.txt'
    s1 = 0
    s2 = 0
    s3 = 0
    s4 = 0
    for k in numbers:
        if float(k)%25.73 == 0:
            s1 = s1 + float(k)/25.73
        elif float(k)%44.18 == 0:
            s2 = s2 + float(k)/44.18

        elif float(k)%12.86 == 0:
            s3 = s3 +float(k)/12.86
        elif float(k)%25.72 == 0:
            s4 = s4 +float(k)/25.72
        else :
            continue
    hejilist = hejishu.split(',')
    if len(hejilist) == 2:
        heji = int(hejilist[0]) * 1000 + float(hejilist[1])
    else:
        heji = float(hejilist[0])

    if round(s1*25.73+s2*44.18+12.86*s3+25.72*s4,2)==heji:
        with open('renshu.txt','w') as f:
            f.write('总金额是{}元\n'.format(heji))
            f.write('25.73有{}个\n'.format(s1))
            f.write('44.18有{}个\n'.format(s2))
            f.write('12.86有{}个\n'.format(s3))
            f.write('25.72有{}个\n'.format(s4))
            f.write('总人数有{}人\n'.format(s1 + s2 + s3 + s4))

            print('25.73有{}个'.format(s1))
            print('44.18有{}个'.format(s2))
            print('12.86有{}个'.format(s3))
            print('25.72有{}个'.format(s4))
            print('总人数有{}人'.format(s1 + s2 + s3 + s4))
    else :
        print('计算有误')

    return renshufilename


def main():
    msg = '请点选OperaPrint.pdf文件'
    print(msg)
    fname = easygui.fileopenbox(msg)
    filename = writeDangtian(fname)
    numbers,hejishu = matchNumber(filename)
    #print(numbers)
    print(hejishu)
    renshufilename = countGeshu(numbers,hejishu)

    os.system(renshufilename)


if __name__ == '__main__':
    main()


