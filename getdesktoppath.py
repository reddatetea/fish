import os

def GetDesktopPath():
    dirpath =  os.path.join(os.path.expanduser("~"), 'Desktop')
    return dirpath

dirpath = GetDesktopPath()
print(dirpath)
