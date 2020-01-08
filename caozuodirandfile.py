import os

def main():

    str = input('请输入查询字符串：')

    path_name = input('请输入查询路径（默认为当前路径）：')

    if path_name == '':

        path_name = '.'

    def file_name(path, str):

        for x in os.listdir(path):

            path_x = os.path.join(path, x)

            if os.path.isfile(path_x) and str in x:

                print (path_x)

            elif os.path.isdir(path_x):

                file_name(path_x, str)

    file_name(path_name , str)

if __name__ == '__main__':

    main()