# 定义一个类，内含私有成员变量和私有成员方法

class Phone:

    __current_voltage = 0.3   # 当前手机运行电压

    def __keep_single_core(self):
        print("让CPU以单核模式运行。")

    def call_by_5g(self):
        if self.__current_voltage >= 1:
            print("5g通话已开启")
        else:
            self.__keep_single_core()
            print("电量不足，无法使用5g，并设置为单核模式以进行省电。")
# 无法被类对象使用
# phone = Phone()
# print(phone.__current_voltage)

phone = Phone()
phone.call_by_5g()