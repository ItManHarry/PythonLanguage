#文件写入
import os
with open('file.txt', 'wb') as f:
    f.writelines((('远看山有色，' + os.linesep).encode('gbk'),('近听水无声。' + os.linesep).encode('gbk'),('春去花还在，' + os.linesep).encode('gbk'),('人来鸟不惊。' + os.linesep).encode('gbk')))
#按照字节读取文件
#read(n):n为字节数，不设置默认读取全部
with open('file.txt', 'rb') as f:
    data = f.read()
    #字节转化字符串 str函数
    print(str(data, 'gbk'))
    # 字节转化字符串 decode函数
    print(data.decode('gbk'))
#安装字符读取文件
with open('file.txt', 'r') as f:
    data = f.read()
    print(data)
#按行读取文件
#readline([n]):读取一行内容，如果指定了参数n则读取改行的n个字符
with open('file.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        print('>', line)
#readlines():读取所有行
with open('file.txt') as f:
    lines = f.readlines()
    print(lines)
    for line in lines:
        print('-', line)