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

def outer(logo):

    def inner(msg):
        print(f"<{logo}>{msg}<{logo}>")

    return inner


fn1 = outer("黑马程序员")
fn1("大家好")
fn1("大家好")

fn2 = outer("传智教育")
fn2("大家好")