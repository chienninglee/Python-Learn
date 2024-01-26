"""
演示判断语句的嵌套使用
"""

# if int(input("您的身高是多少：")) > 120:
#     print("升高超出限制，不可以免费！")
#     print("但是，如果VIP级别大于3，就可以免费")
#
#     if int(input("你的VIP级别是多少:")) > 3:
#         print("恭喜你，VIP级别达标，可以免费")
#     else:
#         print("Sorry，你需要购票66元。")
# else:
#     print("欢迎您，小朋友，可以免费游玩。")
#

age = 18
year  = 1
level = 18
if age >= 18:
    print("您是成年人")
    if age <30:
        print("您的年龄达标了")
        if year > 2:
            print("恭喜你，年龄和入职时间都达标，可以领取礼物")
        elif level >3:
            print("恭喜你，年龄和级别达标，可以领取礼物。")
        else:
            print("不好意思，尽管年龄达标，但是入职时间和级别都不达标")
    else:
        print("不好意思，年龄太大了")

else:
    print("不好意思，小朋友不可以领取。 ")
