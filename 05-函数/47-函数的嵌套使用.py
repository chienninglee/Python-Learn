"""
函数的嵌套使用
"""
#定义函数fun_b
def func_b():
    print("---2---")

#定义函数func_a，并在内部调用fun_b
def func_a():
    print("---1---")

    #嵌套调用func_b
    func_b()

    print("---3---")

#调用函数func_a
func_a()
