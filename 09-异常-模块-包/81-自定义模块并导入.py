# 演示 自定义模块


# 导入自定义模块使用
# import my_module1
# my_module1.test(1,2)

# 导入不同模块的同名功能
# from my_module1 import test
# from my_module2 import test
# test(1,2)

# 　＿＿main＿＿变量
# from my_module1 import test

# 　＿＿all＿＿变量
from my_module1 import *
test_a(1,2)
test_b(1,2)