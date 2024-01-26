my_str = "万过薪月，员序程马黑来，nohtyp学"

#result = my_str[::-1]

result2 = my_str[9:4:-1]
print(f"方法1：结果:{result2}")

result3 =  my_str[5:10][::-1]
print(f"方法2：结果:{result3}")

result4 = my_str.split("，")[1].replace("来","")[::-1]
print(f"方式3：结果：{result4}")