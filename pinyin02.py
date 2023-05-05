import pypinyin

gongyingshangs = ['武汉瑞齐达纸业', '武汉紫兴供应链管理有限公司', '武汉市源兴纸业有限公司', '湖北金光纸业', '武汉美牛纸张物资有限公司', '河南省江河纸业有限公司', '千江']
gys_pinyins = []
for gongyingshang in gongyingshangs:
    gys_ = pypinyin.pinyin(gongyingshang,style=pypinyin.NORMAL)
    print(gys_)
    gys_pinyin = ''.join(i[0]  for i in gys_)
    print(gys_pinyin)
    gys_pinyins.append(gys_pinyin)

print(gys_pinyins)
gys_dic = dict(zip(gongyingshangs,gys_pinyins))
print(gys_dic)

gys = [gys_dic[gongyingshang] for gongyingshang in gongyingshangs]
print(gys)

gongyingshangs.sort(key = lambda gongs : gys_dic[gongs])
print(gongyingshangs)



