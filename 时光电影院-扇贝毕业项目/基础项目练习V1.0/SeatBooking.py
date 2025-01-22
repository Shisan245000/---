# _*_ coding:utf-8 _*_
# 开发人员：Asa
# 开发时间：2025-01-2014:43
# 文件名:SeatBooking.py
# 开发工具:PyCharm
# ...
# ...
import time

class SeatBooking:
    #展示预订状态
    def check_bookings(self, seats):
        print("正在为您查询该场次电影的预订状态...")
        time.sleep(0.7)
        print("从上到下为 1～6 排，从左至右为 1～8 座")
        # 为了让输出结果更美观，额外打印两行分隔线
        print("=" * 32)
        # 逐行打印座位表中的预订信息
        for row in seats:
            time.sleep(0.1)
            print("".join(row))
        print("=" * 32)
        time.sleep(0.7)

    #预订指定座位
    def book_seat(self,seats):
        # 获取用户输入，转换为二维列表的行索引和列索引
        row = int(input("预订第几排的座位呢？请输入 1～6 之间的数字"))-1
        column = int(input("预订这一排的第几座呢？请输入 1～8 之间的数字"))-1

        #如果列表中对应值为 '○' 则预订成功，否则预订失败
        if seats[row][column] =="○":
            print("正在为您预订指定座位...")
            time.sleep(0.7)
            seats[row][column] = "●"# 预订成功，该座位将被标记为“已预约”
            print("预订成功！座位号：{}排{}座".format(str(row + 1), str(column + 1)))
        else:
            print("这个座位已经被预订了哦")

