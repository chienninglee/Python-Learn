# 面向对象类中的成员方法定义和使用

#定义一个带有成员方法的类
class Student:
    name = None     #学生的名字

    def say_hi(self):
        print(f"大家好，我是{self.name},练习时长两年半的偶像练习生。")

    def say_hi2(self,msg):
        print(f"大家好，我是{self.name},{msg}")

stu = Student()
stu.name = "cxk"
stu.say_hi2("哎呦不错哦！")

stu2 = Student()
stu2.name = "蔡徐坤"
stu2.say_hi2("前途无量呀，小朋友！")