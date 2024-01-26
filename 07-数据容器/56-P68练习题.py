"""
元组的基本操作
"""

t1 = ('周杰伦',11,['football','music'])
print(f"{t1}")

#查询年龄所在下标的位置
index = t1.index(11)
print(f"年龄所在下标的位置是：{index}")

#查询学生的姓名
name = t1[0]
print(f"学生的姓名是：{name}")

#删除学生爱好中的football
t1[2][1] =''
print(f"{t1}")

#增加爱好：coding到爱好list内
t1[2][1] = 'coding'
print(f"{t1}")

