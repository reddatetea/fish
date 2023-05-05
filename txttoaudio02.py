# -*- coding:utf-8 -*-
from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '23662984'  # 设置自己创建百度云应用时的ID
API_KEY = 'x9hAww8ilXdBTmF7xW3tiBmg'  # 设置自己创建百度云应用时的APIKey
SECRET_KEY = 'HBKtzrI9RvUFWM4TU9NPWbsU4ouSUi3H'  # 设置自己创建百度云应用时的SECRETKey

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
for i in range(4):
    if (i == 0):
        content = '你瞅啥？'
    if (i == 1):
        content = '瞅你咋地。'
    if (i == 2):
        content = '再瞅一个试试！'
    if (i == 3):
        content = '试试就试试。'
    if (i == 0 or i == 2):
        result = client.synthesis(content, 'zh', 1, {'spd': 0, 'vol': 5, 'per': 3})
    if (i == 1 or i == 3):
        result = client.synthesis(content, 'zh', 1, {'spd': 0, 'vol': 5, 'per': 4})
    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    filename = str(i)
    if not isinstance(result, dict):
        with open('文件的保存路径' + filename + '.mp3', 'wb') as f:
            f.write(result)
