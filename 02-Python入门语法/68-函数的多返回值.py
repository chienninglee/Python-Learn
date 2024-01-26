"""
演示函数的多返回值示例
"""

# 演示使用多个变量，接受多个返回值
def test_return():
    return 1,"hello",True

x,y,z = test_return()
print(x)
print(y)
print(z)