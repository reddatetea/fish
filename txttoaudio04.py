from aip import AipSpeech

APP_ID = '23662984'  # 设置自己创建百度云应用时的ID
API_KEY = 'x9hAww8ilXdBTmF7xW3tiBmg'  # 设置自己创建百度云应用时的APIKey
SECRET_KEY = 'HBKtzrI9RvUFWM4TU9NPWbsU4ouSUi3H'  # 设置自己创建百度云应用时的SECRETKey

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 中文：zh 粤语：ct 英文：en

result = client.synthesis('哈哈哈哈', 'zh', 1, {
    'vol': 5, 'per': 4
})

#识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('audio.mp3', 'wb') as f:
        f.write(result)
