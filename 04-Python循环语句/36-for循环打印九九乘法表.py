#通过外层循环控制行数
for i in range(1,10):
    #通过内层循环控制每一行的数据
    for j in range(1,i+1):
        #在内层循环中输出每一行的内容
        print(f"{j}*{i}={i*j}\t",end='')

    #print()可以输出一个回车符
    print()

