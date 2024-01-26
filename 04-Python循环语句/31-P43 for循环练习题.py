"""
数一数有几个a
"""

name = "Today is Monday"
count = 0

for x in name:
    if x == "a":
        count +=1

print(f"字符串'{name}'中一共有{count}个a。")