'将excel老版本xls文件升级为xlsx文件，以便在openpyxl中操作'
import win32com.client as win32

path=input('请输入带文件路径:')
name = input('请输入文件名:')
fname = path+'/'+name+'.xls'

excel = win32.gencache.EnsureDispatch('Excel.Application')
wb = excel.Workbooks.Open(fname)
wb.SaveAs(fname+"x", FileFormat = 51)
wb.Close()
excel.Application.Quit()

