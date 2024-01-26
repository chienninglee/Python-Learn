"""
ATM
"""

money = 5000000
name = None

name = input("请输入您的名字：")

def balance(show_header):
    if show_header:
        print("-------------查询余额---------------")
    print(f"{name}，你好，您当前余额为{money}元。")


def deposit(num):
    print("---------------存款-----------------")

    global money
    money += num
    print(f"{name}，你好，您的余额为：{money}")
    balance(False)

def withdraw(num):
    global money
    money -= num
    print("---------------取款-----------------")
    print(f"{name}，你好，您已取款：{num}")
    balance(False)

def menu():
    print("--------------主菜单----------------")
    print(f"{name}，你好，欢迎来到ATM，请选择操作")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return input("请输入您的选择：")

#设置无限循环，确保程序不退出
while True:
    keyboard_input = menu()
    if keyboard_input == "1":
        balance(True)
        continue    #通过continue继续下一次循环，一进来就是回到了主菜单
    elif keyboard_input == "2":
        num = int(input("你想要存多少钱？请输入："))
        deposit(num)
        continue

    elif keyboard_input == "3":
        num = int(input("你想要取多少钱？请输入："))
        withdraw(num)
        continue
    else:
        print("程序退出了！")
        break #通过break退出循环。