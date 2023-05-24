#梨视频网页视频网址正则匹配
import re
import requests
url = 'https://www.pearvideo.com/video_1663242'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}
html = requests.get(url,headers = headers).text
#print(html)


r = r'srcUrl="(.*)",vdoUrl=srcUrl'



#编绎时不要忘记re
pattern = re.compile(r)

result = pattern.search(html)

print(result.group(1))

