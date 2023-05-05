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
            else:
                continue


    with open(filename, 'r') as f:
        for hang in f.readlines():
            mat1 = regex1.search(hang)
            if mat1 :
                hejishu = mat1.group(1)
            else :
                continue



    numbers = [float(j) for j in numbers]
    return numbers,hejishu

def countGeshu(numbers,hejishu):
    #print(numbers)
    renshufilename = 'renshu.txt'
    rs2573g1,rs4418g1,rs1286g1,rs2572g1= 0,0,0,0
    rs2573g2,rs4418g2,rs1286g2,rs2572g2= 0,0,0,0

    for k in numbers :
        if  k==25.73 :
            rs2573g1 = rs2573g1+1
        elif k == 44.18:
            rs4418g1 = rs4418g1 + 1
        elif k == 12.86:
            rs1286g1 = rs1286g1 + 1
        elif k == 25.72:
            rs2572g1 = rs2572g1 + 1
        else :
            if  k%25.73 == 0:
                rs2573g2 =k / 25.73 + rs2573g2
            elif  k%44.18 == 0:
                rs4418g2 = k / 44.18+rs4418g2
            elif  k % 25.72 == 0:
                rs2572g2 =  k / 2572 + rs2572g2
            elif  k % 12.86 == 0:
                rs1286g2 = k / 12.86 + rs1286g2
            else :
                continue

    rs2573g = rs2573g1 +rs2573g2
    rs4418g = rs4418g1 + rs4418g2
    rs1286g = rs1286g1 + rs1286g2
    rs2572g = rs2572g1 + rs2572g2
    #print(rs2573g,rs4418g,rs1286g,rs2572g)

    hejilist = hejishu.split(',')
    if len(hejilist) == 2:
        heji = int(hejilist[0]) * 1000 + float(hejilist[1])
    else:
        heji = float(hejilist[0])

    if round(rs2573g*25.73+rs4418g*44.18+12.86*rs1286g+25.72*rs2572g,2)==heji:
        with open('renshu.txt','w') as f:
            f.write('总金额是{}元\n'.format(heji))
            f.write('25.73有{}个\n'.format(int(rs2573g)))
            f.write('44.18有{}个\n'.format(int(rs4418g)))
            f.write('12.86有{}个\n'.format(int(rs1286g)))
            f.write('25.72有{}个\n'.format(int(rs2572g)))
            f.write('总人数有{}人\n'.format(int(rs2573g + rs4418g + rs1286g + rs2572g)))

            print('25.73有{}个'.format(int(rs2573g)))
            print('44.18有{}个'.format(int(rs4418g)))
            print('12.86有{}个'.format(int(rs1286g)))
            print('25.72有{}个'.format(int(rs2572g)))
            print('总人数有{}人'.format(int(rs2573g + rs4418g + rs1286g + rs2572g)))
        os.system(renshufilename)
    else :
        print('计算有误')
        print('25.73有{}个'.format(int(rs2573g)))
        print('44.18有{}个'.format(int(rs4418g)))
        print('12.86有{}个'.format(int(rs1286g)))
        print('25.72有{}个'.format(int(rs2572g)))
        print('总人数有{}人'.format(int(rs2573g + rs4418g + rs1286g + rs2572g)))


    return renshufilename


def main():
    msg = '请点选OperaPrint.pdf文件'
    print(msg)
    fname = easygui.fileopenbox(msg)
    filename = writeDangtian(fname)
    numbers,hejishu = matchNumber(filename)
    #print(numbers)
    print(('总金额是{}元\n'.format(hejishu)))
    renshufilename = countGeshu(numbers,hejishu)




if __name__ == '__main__':
    main()


