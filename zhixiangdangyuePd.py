'''
本模块是从流水账中将纸箱入库数据引入
'''
# _*_ coding:utf-8 _*_
import pandas as pd
import os
import datetime
import zhixiangtodic
import zhixiangdanjiajisuan

def zhixiangDangyue(qijian):
    dtrq = datetime.date.today().strftime('%Y%m%d')    #当天日期
    qishu = qijian[2:4] + qijian[-2:]
    path = r'F:\a00nutstore\006\zw\ZHIXIANG'
    os.chdir(path)
    filename = '纸箱当月入库%s.xlsx'%dtrq
    fname = os.path.join(path, filename)
    jianchen = {'武汉市九安源纸业有限公司':'九安源',
                '恒龙包装':'恒龙',
                '孝感鑫荣环保包装':'孝感鑫荣',
                '武汉市鑫龙鑫纸品有限':'鑫龙鑫限',
                '武汉绿盒子实业':'绿盒子',
                '湖北雷合实业': '雷合',
                '湖北恒大包装':'恒大',
               '湖北梓熠纸制器有限公司':'梓熠'
                }
    price_dic = zhixiangdanjiajisuan.priceDic()
    fname2 = r'F:\a00nutstore\006\zw\原材料实时流水账\原材料实时流水账.xlsx'
    df = pd.read_excel(fname2, sheet_name='流水账',usecols=[0,1,2,3,5,6,7,9,10])    #usecols直接取所取的行
    df = df.loc[df['期间']==qijian ]
    df = df.loc[df['供货单位'].isin (jianchen)] #isin非常实用
    df.insert(3,'箱型',df['品名'])
    for j in ['长', '宽', '高', '长*宽*高', '适装产品'][::-1] :
        df.insert(5,j,None)
    df = df.iloc[:,:-2]     #去掉最后两列，pricename，期间
    for j in ['单个面积', '面积','制版费', '合同单价', '合同金额'][::-1]:
        df.insert(11, j, 0.0)
    for j in [ '多计', '多计金额', '备注']:
        df[j] = 0.0                             #0.0是flaost64,0是ind64
    df [ '备注'] = None
    zhixiangdic = zhixiangtodic.zhixiangdic()                   #生成纸箱字典
    df['长'] = df['箱型'].map(lambda x:zhixiangdic.get(x,(0,0,0))[0])                 #分别根据字典取长宽高的值
    df['宽'] = df['箱型'].map(lambda x:zhixiangdic.get(x,(0,0,0))[1])
    df['高'] =df['箱型'].map(lambda x:zhixiangdic.get(x,(0,0,0))[2])
    df['长*宽*高'] =df['长'].map(str)+'*'+df['宽'].map(str)+'*'+df['高'].map(str)                     #str在前面不行！
    df['类别'] = df['箱型'].map(lambda x:zhixiangdanjiajisuan.zhixiangLeibian(x))
    df['单个面积'] = (df['长'] + df['宽'] + 80) / 1000 * (df['宽'] + df['高'] + 50) / 1000 * 2
    df['面积'] =df['单个面积'] * df['入库数量']
    df = df.assign(singlePrice = df.apply(lambda x : price_dic[x.供货单位][x.类别],axis=1)) #加单价列！新芭解答！
    df['合同单价'] = round(df['单个面积'] * df['singlePrice'],2)
    df['合同金额'] = round(df['合同单价'] * df['入库数量'], 2)
    df['多计'] = df['入库单价'] - df['合同单价']
    df['多计金额'] = df['入库金额'] - df['合同金额']
    grouped = df.groupby('供货单位')
    with pd.ExcelWriter(fname)  as writer:
        df = df.append(df.sum(numeric_only=True),ignore_index=True)
        # df.iloc[df.shape[0]+1,1]='合计'
        df.to_excel(writer, '当月正', index=False)
        for gys, values in grouped:
            gys = jianchen[gys]
            values1 = values.copy()
            values1.loc['合计', '日期'] = '合计'
            values1.at['合计', '入库数量'] = sum(values['入库数量'])
            values1.at['合计', '入库金额'] = sum(values['入库金额'])
            values1.at['合计', '合同金额'] = sum(values['合同金额'])
            values1.at['合计', '多计金额'] = sum(values['多计金额'])
            values1.to_excel(writer, sheet_name='{}{}'.format(gys, qishu),index=False)
    return fname

def main():
    qijian = input('请输入期间：格式为2021-10：\n')
    fname  = zhixiangDangyue(qijian)
    os.startfile(fname)

if __name__ == '__main__':
    main()



















