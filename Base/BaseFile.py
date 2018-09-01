__author__ = 'shikun'

import os


'''
操作文件
'''


def write_data(f, method='w+', data=""):
    if not os.path.isfile(f):
        print('文件不存在，写入数据失败')
    else:
        with open(f, method, encoding="utf-8") as fs:
            fs.write(data + "\n")


def mkdir_file(f, method='w+'):
    if not os.path.isfile(f):
        with open(f, method, encoding="utf-8") as fs:
            print("创建文件%s成功" % f)
            pass
    else:
        print("%s文件已经存在，创建失败" % f)
        pass


def remove_file(f):
    if os.path.isfile(f):
        os.remove(f)
    else:
        print("%s文件不存在，无法删除" % f)


def readTemplate(path):
    with open(path,encoding='UTF-8') as f:
        try:
            data = f.read()
        except EOFError:
            data = False
            print("读取文件错误")
    # print("------read-------")
    #print(data)
    return data

if __name__== "__main__":
    read(r"E:\appium\appium-master\appium-test\Report\result.html")
