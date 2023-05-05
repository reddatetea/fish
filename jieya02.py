import os
import glob
import zipfile

jieyapath =r'Q:\设置\sina\ANSP-PICS\ANSP-PICS-011-CE\ANSP-PICS-011-CE\E-041-043-052'
for j in os.listdir(jieyapath):
    print(j)
    for i in glob.glob('{}\*.zip'.format(os.path.join(jieyapath,j))):
        print(i)
        fileUnZip = zipfile.ZipFile(i)
        zimulu = os.path.join(jieyapath,j)
        print(zimulu)
        fileUnZip.extractall(zimulu)
        fileUnZip.close()
# fileUnZip = zipfile.ZipFile(jieyapath)
# fileUnZip.extractall(r'Q:\设置\sina\ANSP-PICS\ANSP-PICS-011-CE\ANSP-PICS-011-CE\C-149-170-209\1116-Chloe Ho')
# fileUnZip.close()
