# 捕获异常

# 基本捕获语法
try:
    f = open("/09-异常-模块-包/78abc.txt", "r", encoding="UTF-8")
except:
    print("出现异常了，因为文件不存在，我将open的模式，改为w模式去打开")
    f =open("/09-异常-模块-包/78abc.txt", "w", encoding="UTF-8")

# 捕获指定的异常
try:
    print(name)
    #1/0
except NameError as e:
    print("出现变量未定义的异常")
    print(e)

# 1/0     # ZeroDivisionError: division by zero
#print(name)     #NameError: name 'name' is not defined

# 捕获多个异常
try:
    print(name)
    #1/0
except (NameError,ZeroDivisionError) as e:
    print("出现变量未定义 or 除以0的 的异常")


#　未正确设置捕获异常类型，将无法捕获异常

# 捕获所有异常
try:
    open("/09-异常-模块-包/78abcde.txt", "r", encoding="UTF-8")
except Exception as e:
    print("出现异常了")
    open("/09-异常-模块-包/78abcde.txt", "w", encoding="UTF-8")
else:
    print("很高兴，未出现异常！")
finally:
    print("我是finally，有无异常我都会执行。")
    f.close()