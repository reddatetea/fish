'''
查询天干地支排位,以壬子为1
'''
import easygui


def xunhuan(tg_dz, changdu, dizhi_xuhao, tiangan_xuhao):
    tiangan = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
    dizhi = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
    tg = tiangan[tiangan_xuhao % 10 - 1]
    dz = dizhi[dizhi_xuhao % 12 - 1]
    tg_dz.append(tg + dz)
    tiangan_xuhao += 1
    dizhi_xuhao += 1
    changdu = len(tg_dz)
    return tg_dz, changdu, dizhi_xuhao, tiangan_xuhao

def tianganDizhiSort():
    dizhi_xuhao = 1
    tiangan_xuhao = 1
    changdu = 0
    tg_dz = []
    n = 0
    while changdu < 60:
        tg_dz, changdu, dizhi_xuhao, tiangan_xuhao = xunhuan(tg_dz, changdu, dizhi_xuhao, tiangan_xuhao)

    print(tg_dz)
    n = 13

    xh = []
    while n < 74:
        if n < 60 :
            xh.append(n)
        else :
            xh.append(n%60)
        n += 1
    tgdz_xh = dict(zip(tg_dz,xh))
    xh_tgdz = dict(zip(xh,tg_dz))
    print(tgdz_xh,xh_tgdz)
    return tgdz_xh,xh_tgdz

def tgdzSort(tgdz_xh,tgdz):
    paiming = tgdz_xh.setdefault(tgdz,'没有此天干地支的配合')
    print('{}:{}'.format(tgdz, paiming))
    return paiming

def choice_tgdz():
    tiangan = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
    dizhi = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
    msg = '请点选天干'
    print(msg)
    tg = easygui.choicebox(msg, choices=tiangan)
    msg = '请点选地支'
    print(msg)
    dz = easygui.choicebox(msg, choices=dizhi)
    tgdz = tg + dz
    print('你选择的天干地支是:',tgdz)
    return tgdz

def jisuanYearTgdz(nian,xh_tgdz):
    dizhi = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
    xh = (49+(nian - 1840)%60)%60     #1840年是庚子年
    tgdz = xh_tgdz[xh]
    dz = list(tgdz)[-1]
    print('你查询年份的天干地支是:',tgdz)
    shuxiang = ['鼠', '牛', '虎', '兔', '龙', '蛇', '马', '羊', '猴', '鸡', '狗', '猪']
    dz_sx = dict(zip(dizhi,shuxiang))
    print('你查询年份的属相是:', dz_sx[dz])
    return tgdz,dz_sx

def main():
    tiangan = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
    dizhi = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
    tgdz_xh,xh_tgdz = tianganDizhiSort()
    #paiming = tgdzSort(tgdz_xh)
    msg = '请输入要查询的年份\n'
    nian = int(input(msg))
    jisuanYearTgdz(nian,xh_tgdz)

if __name__ == '__main__':
    main()

