import openpyxl
import re

def kaibie(string):
  if '对开' in string :
      zhang = 1000
  elif '三开' in string :
      zhang = 1500
  elif  '全开' in string:
      zhang = 500
  else :                      #四开
      zhang = 2000
  return zhang

def main():
    string = '三开'
    zhang =kaibie(string)
    print(zhang)

if __name__ == '__main__':
    main()
