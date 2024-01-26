# 演示python pymysql库的基础操作
from pymysql import Connection

# 构建到MySql数据库的链接
conn = Connection(
    host = "localhost" ,#主机名（ip）
    port = 3306,        #端口
    user = "root",      #账户
    password = "root"   #密码
)
# print(conn.get_server_info())
# 执行非查询性质SQL
cursor = conn.cursor()  # 获取到游标对象
# 选择数据库
conn.select_db("test")
# 执行sql
#cursor.execute("create table test_pymysql(id int);")
cursor.execute("select * from student")
result = cursor.fetchall()
print(result)
# 执行查询性质SQL

# 关闭链接
conn.close()