# 演示python pymysql库的数据插入
from pymysql import Connection

# 构建到MySql数据库的链接
conn = Connection(
    host = "localhost" ,# 主机名（ip）
    port = 3306,        # 端口
    user = "root",      # 账户
    password = "root",  # 密码
    autocommit = True   # 自动提交（确认）
)

cursor = conn.cursor()  # 获取到游标对象
# 选择数据库
conn.select_db("test")
# 执行sql
cursor.execute("insert into student values(9,'古力娜扎',34,'女')")

# # 通过commit确认
# conn.commit()

# 关闭链接
conn.close()