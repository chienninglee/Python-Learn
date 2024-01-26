staff_inf_dict = {
    "王力宏":{
        '部门':'科技部',
        '工资':3000,
        '级别':1,
    },
    "周杰伦":{
        '部门': '市场部',
        '工资': 5000,
        '级别': 2,
    },
    "林俊杰":{
        '部门': '市场部',
        '工资': 7000,
        '级别': 3,
    },
    "张学友":{
        '部门': '科技部',
        '工资': 4000,
        '级别': 1,
    },
    "刘德华":{
        '部门': '市场部',
        '工资': 6000,
        '级别': 2,
    }
}
print(f"全体员工当前信息如下：{staff_inf_dict}")

for name in staff_inf_dict:
    if staff_inf_dict[name]['级别'] == 1:
        employee_info_dict = staff_inf_dict[name]
        employee_info_dict["级别"] = 2
        employee_info_dict["工资"] += 1000

        staff_inf_dict[name] = employee_info_dict

print(f"全体员工级别为1的员工，完成升职加薪操作后：{staff_inf_dict}")