# #演示循环中断语句continue
# for i in range(1,6):
#     print("sentence1")
#     continue
#     print("sentense2")
#

# 演示continue的嵌套应用
# for i in range(1,6):
#     print("语句1")
#     for j in range(1,6):
#         print("语句2")
#         continue
#         print("语句3")
#
#     print("语句4")
#

# 演示循环语句中断语句 break
# for i in range(1,101):
#     print("语句1")
#     break
#     print("语句2")
#
# print("语句3")


# 演示 break 的嵌套应用
for i in range(1,6):
    print("语句1")
    for j in range(1,6):
        print("语句2")
        break
        print("语句3")

    print("语句4")