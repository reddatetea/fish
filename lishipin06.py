# -*- coding = utf-8 -*-
import requests 
import re
from urllib.request import urlretrieve
import datetime
import time
import os 


url = 'https://www.pearvideo.com/video_1738789'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}

def geturl(url):
    res = requests.get(url, headers = headers)

    resp =res.text

    #print(res.status_code)
    if res.status_code == 200 :
        print('请求成功')
        #print(res.text)
    else:
        print('请求失败')
    return resp


resp = geturl(url)
r = '(?:<a href="video_)(.*)(?:" class="vervideo-lilink actplay">)'
pattern = re.compile(r)
urlLists = pattern.findall(resp)
#print(urlLists)

#当天日期
dtrq = datetime.date.today().strftime('%Y%m%d')
print(dtrq)
path = 'D:\\y娱乐\\梨视频'
os.chdir(path)

with open('梨视频下载%s.txt'%dtrq,'w') as f :
    for i in urlLists :
        url = 'https://www.pearvideo.com/'+ 'video_' + i
        resp = geturl(url)
        print(url)

        print(resp)
        #r = 'srcUrl="https://video.pearvideo.com/mp4/adshort/20200323/cont-1663688-15033970_adpkg-ad_hd.mp4",vdoUrl=srcUrl'
        #src="https://video.pearvideo.com/mp4/adshort/20201019/cont-1702384-15436461_adpkg-ad_hd.mp4"
        r1 = '(?:src=")(.*)(?:mp4")'
        pattern1 = re.compile(r1)
        # urlList02 = pattern1.search(resp)
        urlList02 = pattern1.search(resp).group(1)

        urlList02 = urlList02 + 'mp4'
        print(urlList02)




        #r2= '<h1 class="video-tt">苹果Siri增加新冠病毒检测功能，还能自动为用户呼叫911</h1>'
        r2 = '<h1 class="video-tt">(.*)</h1>'
        pattern2 = re.compile(r2)
        title = pattern2.search(resp).group(1)
        print(title)

        f.write('%s\n '%title)
        f.write('%s\n '%urlList02)
        f.write('  \n')


        #下载视频
        filePath = path+title+'.mp4'
        urlretrieve(urlList02,title+'.mp4')

        time.sleep(1)


    












