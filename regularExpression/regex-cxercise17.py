'''
原材料品名按标准格式命名，将不规范的命名通过正则表达式改为标准命名
涉及正则表达式的命名(?P<>...)
?:...非捕获组
'''
import requests
import re
url = 'https://www.amazon.cn/gp/bestsellers/digital-text/116169071/ref=sv_kinc_4'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36','cookie' :''
,'cookie':'session-id=458-2251486-3510343; ubid-acbcn=461-9219891-2213330; lc-acbcn=zh_CN; x-wl-uid=18zI1bCffoFjVZ7CZh92c2sSyFYB56j4q0GqrNmVN3T1S/DvcChVkw9Xw55yjZO9dRWe1IBrb+H7R7xmllCNLa0DBcuPXun0OB3lffLG2Yt5H9qVa4jr+tOXP0OQdh9jGpvD+bZOE/eI=; x-acbcn="NxKiLLh@WofBZPDBEQdbuOCjtVpe3tbs"; at-main=Atza|IwEBIEJu8JH2P95wsJ0_ogpC7ErOZA7hJyLcK3M6QBPULGbqtEU0y6Psa6x17_h0O54NfRCI02iPEkd3PsuNeITutW_pAc4DA_ujixnvZJ7d5JPCL6fS7ofeyZ8iVOXFxM7BdKKAbeEVfra7SimVnyM4kCkN_JXGkQ7cb3RT9PQM2G1qkW4Lb2XvtcX1E-q0PwHnBu6_hjyL3tFvO9PNKDbIaaZrDDs-SFHUDSFwvw2thDEAkXv8qFNUfvu73gbdf8LoLSp2IqEMkEqKzQYRhQCetB7_Lmdfi4hOvL-SNMUEv-Awh-F8DouvtrPEYRtrax0rCOTLbOyAlr3j_jsjjAAhLEp3Tvi0hpDenR9lJwW3syvuZBcLcYI9Ks6vlH3G5pd4hkFF5UYFSZzQmoNnZogqlt1o; sess-at-main="Viwz375uQ+8CiUDlX/dHDEpZQ7E5nVe9u3egwWKIin0="; sst-main=Sst1|PQGEyq33y8RwZcj9I2V0FXQZC-I7nXf-9Ekb0S-rpB3wkebzHrW90Jwsw4gOYGhT60LBUR9oxSA8vYHRn_hPBx4NiY0bAWycjCuM2HVn_fykJiVdnT4L3vuMELAnt_cHhnB3uQJO3szyGwl94HivYBIfwtGZs2bLttYY-KyqZwJipgTgCYTcrHWW1Hzh8olaTf7Z6BR6n7bsJPIFyjnm_l6xORS3_3DRJx65ebyhsadUEMnB5qpWvny0IoGVa-xYGvOpmWZXt92Sypdw2DV07RBZhO8igPNHStsqb7DsaPACXmTeTRXLGVd5GDaGFlholAVHBZr8fo9yxWRJRAwp8LAZGA; i18n-prefs=CNY; session-token="pKAhKdMVjrNK+1JU1D1yBhOlHIQVCf/jjE/0ncAltsB71yUXLFPjp97FzF7GPELhuBTSwv+VP4j8mRPqJMeP1RbVEjTKMn+4FrvMhSZg/tXg7QMPBm7zzRqmNflYHL9WYzYr/6HRzCKtGO+acm9KzhqY/fkCcCKOE7UAFYFuq1TSLD8te1iTIZM2wI1EivKQgKuqo5DP2WgeNrtt/6qwvljUZEDVm7N/P2sbGoQRw/c4XPo1nFhZ+duOKfr+yMQ194R2Wb4PpsA="; session-id-time=2082787201l; csm-hit=tb:s-2RB876GB77231RM0QSBE|1585041152529&t:1585041154430&adb:adblk_no'}

res = requests.get(url, headers = headers)

resp =res.content.decode('utf-8')
#print(resp)
int_string = resp

pattern = r"span class='p13n-sc-price' >￥(\d*\.\d*)</span"
regexp = re.compile(pattern)
'''
def rename(match_obj):
    ke = match_obj(group('ke'))+'g'
    leixing = match_obj(group('leixing'))
    cicun = match_obj(group('cicun'))
    return
'''
a = regexp.findall(int_string)
print(a)




