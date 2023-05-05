import requests
import bs4
import pandas as pd
url = r'https://wh.lianjia.com/ershoufang/xudong/'

Headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3702.0 Safari/537.36'
}
response = requests.get(url, headers = Headers)
#print(response.text)
soup = bs4.BeautifulSoup(response.text)
name = [i.text.strip() for i in soup.findAll(name = 'a', attrs = {'data-el':'region'})]
Type = [i.text.split('|')[0].strip() for i in soup.findAll(name = 'div', attrs = {'class':'houseInfo'})]
size = [float(i.text.split('|')[1].strip()[:-2]) for i in soup.findAll(name = 'div', attrs = {'class':'houseInfo'})]
direction = [i.text.split('|')[2].strip() for i in soup.findAll(name = 'div', attrs = {'class':'houseInfo'})]
ZX = [i.text.split('|')[3].strip() for i in soup.findAll(name = 'div', attrs = {'class':'houseInfo'})]
flool = [i.text.split('|')[4].strip() for i in soup.findAll(name = 'div', attrs = {'class':'houseInfo'})]
year = [i.text.split('|')[5].strip() for i in soup.findAll(name = 'div', attrs = {'class':'houseInfo'})]

total = [float(i.text[:-1]) for i in soup.findAll(name = 'div', attrs = {'class':'totalPrice'})]
price = [int(i.text[2:-4]) for i in soup.findAll(name = 'div', attrs = {'class':'unitPrice'})]

datamessage = pd.DataFrame({'name':name,'Type':Type,'size':size,'direction':direction,'ZX':ZX,
 'flool':flool,'year':year,'total':total,'price':price})

print(datamessage)
