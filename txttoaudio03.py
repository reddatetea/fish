# -*- coding:utf-8 -*-
from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '23662984'  # 设置自己创建百度云应用时的ID
API_KEY = 'x9hAww8ilXdBTmF7xW3tiBmg'  # 设置自己创建百度云应用时的APIKey
SECRET_KEY = 'HBKtzrI9RvUFWM4TU9NPWbsU4ouSUi3H'  # 设置自己创建百度云应用时的SECRETKey

def main(str_input):  # 输入要合成的文字
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)  # 接口调用
    result = client.synthesis(str_input, 'zh', 1, {'spd': 5, 'vol': 5, 'per': 4})  # 进行合成并返回
    ''' spd 语速 0-9 ; vol 音量 0-15 ; per 人声选择 1-4 '''
    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    filename = "sound_result"  # 保存的文件名
    if not isinstance(result, dict):
        with open(filename + '.mp3', 'wb') as f:
            f.write(result)


if __name__ == '__main__':
    main("你好帅啊")