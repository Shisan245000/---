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

    #获取行列索引
    def get_row(self):
        input_row = input("预订第几排的座位呢？请输入 1～6 之间的数字")
        valid_row = [str(i+1) for i in range(6)]
        # 如果用户输入不符合要求，就提醒用户重新输入
        while input_row not in valid_row:
            input_row = input("没有按要求输入哦，请输入 1～6 之间的数字")
        # 将行号转换为二维列表的行索引
        row = int(input_row)-1
        return row

    def get_column(self):
        input_column = input("预订这一排的第几座呢？请输入 1～8 之间的数字")
        valid_column = [str(i + 1) for i in range(8)]
        # 如果用户输入不符合要求，就提醒用户重新输入
        while input_column not in valid_column:
            input_column = input("没有按要求输入哦，请输入 1～8 之间的数字")
        # 将列号转换为二维列表的列索引
        column = int(input_column)-1
        return column

    #预订指定座位
    def book_seat(self,seats):
        # 获取用户输入，转换为二维列表的行索引和列索引
        while True:
            # 重复获取用户输入
            row = self.get_row()
            column = self.get_column()

            if seats[row][column] == "○":
                print("正在为您预订指定座位...")
                time.sleep(0.7)
                seats[row][column] = "●"
                print("预订成功！座位号：{}排{}座".format(row + 1, column + 1))
                break#如果预订成功，就退出选座系统
            else:
                print("预订失败,这个座位已经被预订了哦，试试别的吧")
                time.sleep(0.7)

