# 演示模块的导入

# 使用import导入time模块使用sleep功能（函数）
# import time     #导入python内置的time模块（time.py这个代码文件）
# print("你好")
# time.sleep(5)
# print("我好")


# 使用 from 导入 time 的 sleep 功能（函数）
# from time import sleep
# print("你好")
# sleep(5)
# print("我好")


# 使用 * 导入time模块的全部功能
# from time import *
# print("你好")
# sleep(5)
# print("我好")


# 使用as给特定功能加上别名
# import time as t
# print("你好")
# t.sleep(5)
# print("我好")

from time import sleep as sl
print("你好")
sl(5)
print("我好") 