#方式1：使用print直接输出类型信息
print(type("坚持就是胜利"))
print(type(123456789))
print(type(13.14))

#方法2：使用变量存储type（）语句的结果
str_type=type("坚持就是胜利")
int_type=type(123456)
float_type=type(13.14)

print(str_type)
print(int_type)
print(float_type)

#方法3：使用type（）语句,查看变量中的数据类型信息
name = "坚持就是胜利"
name_type = type(name)
print(name_type)