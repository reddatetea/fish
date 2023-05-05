# ch14_43.py
import zipfile

fileUnZip = zipfile.ZipFile(r'Q:\设置\sina\ANSP-PICS\ANSP-PICS-011-CE\ANSP-PICS-011-CE\C-149-170-209\1116-Chloe Ho\SM0802-Chloe Ho.zip')
fileUnZip.extractall(r'Q:\设置\sina\ANSP-PICS\ANSP-PICS-011-CE\ANSP-PICS-011-CE\C-149-170-209\1116-Chloe Ho')
fileUnZip.close()
