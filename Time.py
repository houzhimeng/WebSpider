import datetime
class test():
# 时间校验
    @staticmethod
    def timeDecorator():
        timestart = datetime.datetime(today().year, today().month, today().day, 0, 0, 0)
        orderend = datetime.datetime(func.today().year, func.today().month, func.today().day, 1, 0, 0)
        timeend = datetime.datetime(today().year, today().month, today().day, 23, 59, 59)
        orderstart = datetime.datetime(func.today().year, func.today().month, func.today().day, 23, 0, 0)
        now = datetime.datetime.now()

test2 = test()

print(test2.timeDecorator())