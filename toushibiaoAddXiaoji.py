import pandas as pd

df=pd.DataFrame({'Region':['Oceanian','Europe','Asia','America','Europe','America','Asia','Oceanian','America'],'Country':["AU","GB","KR","US","GB","US","KR","AU","US"],'Region Manager':['TL','JS','HN','AL','JS','AL','HN','TL','AL'],'Campaign Stage':['Start','Develop','Develop','Launch','Launch','Start','Start','Launch','Develop'],'Product':['abc','bcd','efg','lkj','fsd','opi','vcx','gtp','qwe'],'Curr_Sales': [453,562,236,636,893,542,125,561,371],'Curr_Revenue':[4530,7668,5975,3568,2349,6776,3046,1111,4852],'Prior_Sales': [235,789,132,220,569,521,131,777,898],'Prior_Revenue':[1530,2668,3975,5668,6349,7776,8046,2111,9852]}
               )

table=pd.pivot_table(df, values=['Curr_Sales', 'Curr_Revenue', 'Prior_Sales', 'Prior_Revenue'], index=['Region','Country', 'Region Manager','Campaign Stage','Product'],aggfunc='sum')
out = pd.concat([d.append(d.sum().rename((k, '', '', '', 'Subtotal'))) for k, d in table.groupby('Region')]).append(table.sum().rename(('Grand', '', '', '', 'Total')))
out.index = pd.MultiIndex.from_tuples(out.index)
out.to_excel('gggg.xlsx')