# 演示python闭包的特性

# 简单闭包
# def outer(logo):
#
#     def inner(msg):
#         print(f"<{logo}>{msg}<{logo}>")
#         return inner
#
# fn1 = outer("你好")
# fn1("hello")
#
# fn2 = outer("上午好")
# fn2("hello")

# def outer(logo):
#
#     def inner(msg):
#         print(f"<{logo}>{msg}<{logo}>")
#
#     return inner
#
#
# fn1 = outer("黑马程序员")
# fn1("大家好")
# fn1("hello,everyone")
#
# fn2 = outer("传智教育")
# fn2("aaaaaaaaaaaaaa")
# fn2("bbbbbbbbbbbbbb")

# 使用闭包实现ATM小案例
def account_create(initial_amount=0):
    def atm(num, deposit=True):
        nonlocal initial_amount
        if deposit:
            initial_amount += num
            print(f"存款：+{num}，账户余额：{initial_amount}")
        else:
            initial_amount -= num
            print(f"取款：-{num}，账户余额：{initial_amount}")

    return atm


atm = account_create()
atm(1000)
atm(300, deposit=False)
