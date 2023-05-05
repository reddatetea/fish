import xlwings as xw

def excelAutofit(fname,ws_name):
    app = xw.App(visible=False, add_book=False)
    wb = app.books.open(fname)
    ws = wb.sheets[ws_name]
    ws.autofit()  # 自动适应单元格
    wb.save(fname)
    wb.close()
    app.quit()
    return fname

def main():
    excelAutofit(fname, ws_name)

if __name__ =='__main__':
    main()