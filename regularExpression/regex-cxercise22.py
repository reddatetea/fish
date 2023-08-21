# -*- coding = utf-8 -*-
import re


str = '【全民GIF第三季】看动图涨球技-樊振东VS许昕（2） 1'
#str='昕爷的正手弧圈利器-许氏圆月弯刀 1'


#r = '(.*)\s*（?\d*）?\s*(?:\d*$)'

#r = '(【?\w*[\u4e00-\u9fa5]*\w*[\u4e00-\u9fa5]*】?[\u4e00-\u9fa5]*-[\u4e00-\u9fa5]*)?\d*）?\s*(?:\d*$)'
r = '\S\d*$'

pattern = re.compile(r)

a = pattern.search(str)


print(a.group(1))

