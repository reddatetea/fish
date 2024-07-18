'''
hello git
'''
import codecs
with codecs.open(r"F:\a00nutstore\my note\typoraStudy\你好 Typora.md", "rb", 'utf-8', errors='ignore') as txtfile:
    for line in txtfile:
        print(line)
