'''
查询天干地支排位,以甲子为1
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
    tgdz_sort = dict(zip(tg_dz, range(1, 61)))
    print(tgdz_sort)
    return tgdz_sort

def tgdzSort(tgdz_sort):
    tiangan = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
    dizhi = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
    msg = '请点选天干'
    print(msg)
    tg = easygui.choicebox(msg, choices=tiangan)
    print(msg)
    dz = easygui.choicebox(msg, choices=dizhi)
    tgdz = tg + dz
    paiming = tgdz_sort.setdefault(tgdz,'没有此天干地支的配合')
    print('{}:{}'.format(tgdz, paiming))

def main():
    tiangan = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
    dizhi = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
    tgdz_sort = tianganDizhiSort()
    tgdzSort(tgdz_sort)

if __name__ == '__main__':
    main()

