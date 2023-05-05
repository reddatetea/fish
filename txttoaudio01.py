from aip import AipSpeech
from pydub import AudioSegment
from pydub.playback import play
import io
""" 你的 APPID AK SK """
APP_ID = '23662984'  # 设置自己创建百度云应用时的ID
API_KEY = 'x9hAww8ilXdBTmF7xW3tiBmg'  # 设置自己创建百度云应用时的APIKey
SECRET_KEY = 'HBKtzrI9RvUFWM4TU9NPWbsU4ouSUi3H'  # 设置自己创建百度云应用时的SECRETKey
speech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
"""----------------------------------------------
read_text函数
输入
    text：堂堂你好，堂堂你好
    save：是否保存成音频
    name：如果保存那保存成什么名字

输出
    直接读出音频，成功返回1
----------------------------------------------"""
def read_text(text,save = 1,name ="tangtangnihao"):
    result = speech.synthesis(
    text, # UTF-8编码的文本，小于1024字节
    "zh", # zh/en
    1,)
    #if not isinstance(result, dict):
    #dict0 = {'spd':0,'vol': 5,'per':3}
    if not isinstance(result,dict):
        print('识别成功，正在播放音频')
        voice = AudioSegment.from_file(io.BytesIO(result), format="mp3")
        play(voice)
        if save:
            with open(name+'.mp3', 'wb') as f:
                f.write(result)
        return 1

    else :
        print('转换失败')


# f.write(result)
text = '堂堂你好吗？'
read_text(text,1,'audio')