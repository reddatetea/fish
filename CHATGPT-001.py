import pandas as pd

# 指定文件路径
file_path = "D:/Samples/单品电商数据.xlsx"

# 使用pandas读取Excel文件，指定引擎为"openpyxl"
df = pd.read_excel(file_path, engine="openpyxl")

# 输出数据的形状（行数、列数）
print("数据形状:", df.shape)

# 输出数据的行数
print("行数:", len(df))

# 输出数据的列数
print("列数:", len(df.columns))
