# 演示python 内置的各类魔术方法

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    #__str__魔术方法：字符串
    def __str__(self):
        return f"Student类对象，name：{self.name},age:{self.age}"


    # __lt__魔术方法：大于小于
    def __lt__(self, other):
        return self.age < other.age

    # __le__魔术方法：小于等于比较符号
    def __le__(self,other):
        return self.age <= other.age

    # __eq__魔术方法:比较运算符实现方法
    def __eq__(self, other):
        return self.age == other.age




stu1 = Student("周揭露",42)
stu2 = Student("林俊杰",42)
print(stu1 == stu2)
print(stu1 >= stu2)