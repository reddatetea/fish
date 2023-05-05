import  os
import  easygui

def  searchFile(path,keyname):
    os.chdir(path)
    for file in os.listdir(path):
        if  os.path.splitext(file)[-1] =='.py' :
            with open(file,encoding = 'utf-8') as f:
                for  j in f.readlines():
                    if  keyname  in j :
                        print(os.path.join(path,file))
                        print(j)
                    else :
                        continue

        else :
            continue




def  main():
    msg = '请点选要要查找文件所在文件夹'
    path = easygui.diropenbox(msg)
    keyname = input('请输入要查询文本的关键字\n')
    searchFile(path,keyname)

if  __name__ == '__main__' :
    main()


