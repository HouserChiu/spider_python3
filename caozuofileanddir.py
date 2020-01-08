import os
def search(path,str):   #输入路径，和字符串名称
    for file in os.listdir(path):    #列出当前目录下所有文件及文件夹
        path = os.path.join(path,file)     #将文件路径及该路径下的文件进行合并
        if os.path.isfile(path):       #判断当前路径是目录还是文件
           if str in file:
              print(path)
        else:                                  #如果不是文件就继续递归执行
           search(path,file)

if __name__ == '__main__':
   search(os.path.abspath('.'),'mo')