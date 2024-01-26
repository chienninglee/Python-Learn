# 演示异常出现

# 通过open（），读取一个不存在的文件
f =open("D:/abc.txt","r",encoding="UTF-8")

# Traceback (most recent call last):
#   File "E:\Program\Python-Learn\02-Python入门语法\77-演示异常的出现.py", line 4, in <module>
#     f =open("D:/abc.txt","r",encoding="UTF-8")
# FileNotFoundError: [Errno 2] No such file or directory: 'D:/abc.txt'