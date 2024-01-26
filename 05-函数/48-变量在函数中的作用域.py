#演示局部变量
# def test_a():
#     num = 100
#     print(num)
#
# test_a()
# #出了函数体，局部变量就无法使用了。
# #print(num)

#演示全局变量
#全局变量：在函数外定义的变量
# num = 200
#
# def test_a():
#     print(f"test_a:{num}")
#
# def test_b():
#     print(f"test_b:{num}")
#
# test_a()
# test_b()
# print(num)

#在函数内修改全局变量
num = 200

def test_a():
    print(f"test_a:{num}")

def test_b():
    num = 500
    print(f"test_b:{num}")

test_a()
test_b()
print(num)


#global关键字，在函数内声明
num = 200

def test_a():
    print(f"test_a:{num}")

def test_b():
    global num #设置 内部定义的变量设置为全局变量
    num = 500
    print(f"test_b:{num}")

test_a()
test_b()
print(num)