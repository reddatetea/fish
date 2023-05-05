import pandas as pd
df = pd.DataFrame()
# url_list = ['http://www.espn.com/nba/salaries/_/seasontype/4']
# for i in range(2, 13):
#     url = 'http://www.espn.com/nba/salaries/_/page/%s/seasontype/4' % i
#     url_list.append(url)
#
# #遍历网页中的table读取网页表格数据
# for url in url_list:
#     df = df.append(pd.read_html(url), ignore_index=True)
# #列表解析：遍历dataframe第3列，以子字符串$开头
url = 'https://www.zhcw.com/kjxx/pl3/'
df = df.append(pd.read_html(url), ignore_index=True)
# df = df[[x.startswith('$') for x in df[3]]]
# df.to_csv('排列3pl3.csv',header=['期号','开奖日期','开奖号码'], index=False)
df.to_csv('排列3pl3.csv' ,index=False)
