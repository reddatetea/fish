from aip import AipOcr
import easygui

def ocrSeting():
    APP_ID = '23095509'  # 设置自己创建百度云应用时的ID
    API_KEY = 'djYDLV9BPL53wzeRtodPxBv3'  # 设置自己创建百度云应用时的APIKey
    SECRET_KEY = 'ZyeerHwASUHIrgi0HGzRjCm8Zgvy2ZyG'  # 设置自己创建百度云应用时的SECRETKey
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)  # 创建语音识别对象
    return APP_ID,API_KEY,SECRET_KEY,client

def get_file_content(file):
    with open(file, 'rb') as fp:
        return fp.read()

def img_to_str(image_path,client):
    image = get_file_content(image_path)
    # 通用文字识别（可以根据需求进行更改）
    result = client.basicGeneral(image)
    return result

def main():
    APP_ID, API_KEY, SECRET_KEY, client = ocrSeting()
    #image_path = r'D:\a00nutstore\fishc\ocr测试20210216.png'
    msg = '请点选需要ocr识别的图片文件'
    print(msg)
    image_path = easygui.fileopenbox(msg)
    result = img_to_str(image_path,client)
    print(result)
    for i in result.get('words_result'):
        print(i.get('words'))

if __name__ == '__main__':
    main()

