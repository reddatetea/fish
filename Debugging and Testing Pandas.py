import pandas as pd
import numpy as np
import zipfile
import os
import win32com.client as win32
import xlwings

os.chdir(r'D:\a00nutstore\Pandas-Cookbook-Second-Edition-master')
url = 'data/kaggle-survey-2018.zip'

with zipfile.ZipFile(url) as z:
    print(z.namelist())
    kag = pd.read_csv(z.open('multipleChoiceResponses.csv'))
    df = kag.iloc[1:]

print(df)


