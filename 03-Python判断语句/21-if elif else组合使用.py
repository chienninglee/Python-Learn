"""
演示if elif else多条件判断语句的使用
"""

height = int(input("请输入您的身高cm："))
vip_level = int(input("请输入您的vip等级（1-5）："))
day = int(input("请告诉我今天是几号："))

#通过if判断，可以使用多条件判断的语法
#第一个条件就是if
if height < 120:
    print("身高小于120cm，可以免费游玩")
elif vip_level > 3:
    print("vip级别大于3，可以免费游玩")
elif day == 1:
    print("今天是免费日1号，可以免费游玩")
else:
    print("不好 意思，条件都不满足，需要买票66元！")