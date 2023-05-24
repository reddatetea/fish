'''
用正则将跨越多行的括号连同里面的内容进行删除

'''

# coding = 'utf-8'
import re 

#正则表达式imput_re
regex = r'^\s*（(.*\s\n)*.*）\n'

#编绎正则表达式 re.compile(compile模式)
pattern = re.compile(regex)

#字符串imput_str
imput_str = '''

【释文】十七日先书郗司马未去 即日得足下书为慰先书以 具示复数字，吾前东粗足作佳观吾 为逸民之怀久矣足下何以 
等（方）复及此似梦中语耶无缘言面为叹书何能悉 龙保等平安也谢之甚迟见 卿舅可耳至为简隔也 
今往丝布单衣财一端 示致意计与足下别十六年于今虽 时书问不解阔怀省足下先后 二书但增叹慨顷积雪凝 
寒五十年中所无想顷如 常冀来夏秋间或复得 足下问耳比者悠悠如何可言吾服食久犹为劣劣大都 比之年时为复可可足下保 
（爱为上临书但有惆怅，知足下行至吴念违 离不可居叔当西耶 迟知问 瞻近无缘省苦（告）但有悲叹 
足下小大悉平安也云卿当 来居此喜迟不可言想必 果言苦（告）有期耳亦度，卿当不居京此既避又节 气佳是以欣卿来也此信旨 
还具示问 天鼠膏治耳聋有验不有验者乃是要药 朱处仁今所在往得其 书信遂不取答今因足下答 
其书可令必达 足下今年政七十耶知体气 常佳此大庆也想复愚加颐养吾年垂耳顺推之 人理得尔以为厚幸但恐前 
路转欲逼耳以尔要欲一 游目汶领非复常言足下 但当保护以俟此期勿谓 虚言得果此缘一段奇事 也 
去夏得足下致邛竹杖皆 至此士人多有尊老者皆 即分布令知足下远惠 之至，省足下别疏具彼土山川诸 ）
奇杨（扬）雄蜀都左太冲三 都殊为不备悉彼故为多奇益令其游目意足 也可得果当告卿求迎少 人足耳至时示意迟此 
期真以日为岁想足下镇 彼土未有动理耳要欲 及卿在彼登汶领峨眉 而旋实不朽之盛事但言此心以驰于彼矣 
彼盐井火井皆有不足下 目见不为欲广异闻具示，省别具足下小大问为慰多 分张念足下悬情武昌诸 子亦多远宦足下兼怀 
'''

#sub替换
newname = re.sub(pattern,'',imput_str)
print(newname)








