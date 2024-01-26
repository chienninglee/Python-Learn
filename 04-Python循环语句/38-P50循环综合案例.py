"""
演示循环综合案例：发工资
"""

#定义账户余额变量
money = 10000

#for循环对员工进行发放工资
for i in range(1,21):
    import random
    grade = random.randint(1, 10)
    if grade <5:
        print(f"员工{i},绩效分{grade},低于5，不发工资，下一位。")
        # continue跳过发放
        continue
    if money >=1000:
        money-=1000
        print(f"向员工{i}发放工资1000元，账户余额还剩余{money}元。")

    else:
        print(f"余额不足，当前余额：{money}，不足以发放工资，这次不发了，下次再来。")
        #break结束发放
        break


#break结束发放