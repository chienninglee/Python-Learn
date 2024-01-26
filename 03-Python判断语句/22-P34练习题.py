# 猜猜心理的数字


num = 27
if int(input("请输入第一次猜想的数字：")) == num:
    print("恭喜你，第一次就猜对了")
elif int(input("不对，再猜一次：")) == num:
    print("恭喜你，第二次就猜对了")
elif int(input("不对，再最后猜一次：")) == num:
     print("恭喜你，终于猜对了")
else:
    print("Sorry,全部猜错了，我想的是数字：10")

