# 演示读取文件，课后习题

# 打开文件，以读取模式打开
f = open("/08-文件操作/73word.txt", "r", encoding="UTF-8")

# 方法一：读取全部内容，通过字符串count方法统计itheima单词数量
# content = f.read()
# count = content.count("itheima")
# print(f"itheima在文件中一共出现了：{count}次")

# 方法二：读取内容，一行一行读取
count = 0
for line in f:
    line = line.strip()     #去除开头和结尾的空格以及换行符
    words = line.split(" ")
    for word in words:
        if word == "itheima":
            count += 1

print(f"itheima出现的次数是：{count}")

# 关闭文件
f.close()