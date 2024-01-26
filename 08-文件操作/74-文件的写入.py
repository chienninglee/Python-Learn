# 演示文件的写入

# 打开文件，不存在的文件,mode:r,w,a(r:读取文件，w:覆盖写入,a：追加内容）
import time

# f = open("E:/Program/Python-Learn/02-Python入门语法/74test.txt","w",encoding="UTF-8")
# # write写入
# f.write("Hello World!!!")   #将内容写入到内存中
#
# # flush刷新
# # f.flush()                 #将内存中积攒的内容，写入到硬盘文件中
# # time.sleep(600000)
#
# # close关闭
# f.close()                   #close方法，也内置了flush()功能


# 打开一个存在的文件
f = open("/08-文件操作/74test.txt", "w", encoding="UTF-8")
# write写入，flush刷新
f.write("黑马程序员")
# close关闭
f.close()