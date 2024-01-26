# 构造方法练习
# 学生信息录入

#类
class Studen_info:
    name = None
    age = None
    addr = None

    #成员方法，构造方法
    def __init__(self):
        self.name = input("请输入学生姓名:")
        self.age = int(input("请输入学生年龄:"))
        self.addr = input("请输入学生地址:")

for x in range(1,4):
    print(f"当前录入第{x}位学生信息，总共需要录入3位学生信息。")
    stu = Studen_info()
    print(f"学生{x}信息录入完成，信息为【学生姓名：{stu.name},年龄：{stu.age}，地址；{stu.addr}】")



