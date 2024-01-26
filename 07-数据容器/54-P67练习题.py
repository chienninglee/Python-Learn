"""
取出列表内的偶数
"""

# list = [1,2,3,4,5,6,7,8,9,10]
# index =0
# while index < len(list):
#
#     list.append()
#     print(f"{}")

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# while 循环实现
def while_remove_odd():
    global my_list
    new_list = []
    index = 0
    while index < len(my_list):
        item = my_list[index]
        # 判断是否是偶数
        if item % 2 == 0:
            new_list.append(item)
        index += 1
    print(f"通过while，源列表{my_list},取出偶数后的列表{new_list}")

while_remove_odd()

# for 循环实现
def for_remove_odd():
    global my_list
    new_list = []
    for item in my_list:
        if item % 2 == 0:
            new_list.append(item)
    print(f"通过for，源列表{my_list},取出偶数后的列表{new_list}")

for_remove_odd()