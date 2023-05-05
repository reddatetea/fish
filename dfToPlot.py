import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import xlwings as xw

@xw.func
@xw.arg("df", pd.DataFrame)
@xw.ret(expand='table')
def describe(df):
    return df.describe()

@xw.func
@xw.arg("df", pd.DataFrame)
def plot(df, name, caller):
    plt.style.use("seaborn")
    if not df.empty:
        caller.sheet.pictures.add(df.plot().get_figure(),
                                  top=caller.offset(row_offset=1).top,
                                  left=caller.left,
                                  name=name, update=True)
    return f"<Plot: {name}>"


if __name__ == "__main__":
    haha()
