# 练习案例：常用功能练习
#
# 有一个列表，内容是：[21, 25, 21, 23, 22, 20]，记录的是一批学生的年龄
# 请通过列表的功能（方法），对其进行
#
# 1.
# 定义这个列表，并用变量接收它
# 2.
# 追加一个数字31，到列表的尾部
# 3.
# 追加一个新列表[29, 33, 30]，到列表的尾部
# 4.
# 取出第一个元素（应是：21)
# 5.
# 取出最后一个元素（应是：30)
# 6.
# 查找元素31，在列表中的下标位置

list_age =[21,25,21,23,22,20]
list_age.append(31)
print(f"{list_age}")

list_age2 = [29,33,30]
list_age.extend(list_age2)
print(f"{list_age}")

element = list_age.pop(0)
print(f"{list_age},{element}")

element = list_age.pop(-1)
print(f"{list_age},{element}")

position = list_age.index(31)
print(f"{position}")

