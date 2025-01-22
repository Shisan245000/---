# _*_ coding:utf-8 _*_
# 开发人员：Asa
# 开发时间：2025-01-2015:19
# 文件名:main.py
# 开发工具:PyCharm
# ...
# ...
#导入SeatsBooking类
from SeatBooking import SeatBooking
from infos import infos
from film_selector import FilmSelector
import time
class Controller:
    def __init__(self,infos):
        self.films = infos # 电影库所有电影
        # 打印欢迎语
        self.welcome()
        # 用户选择想观看的电影
        self.choose_film()
        # 根据用户选择，执行不同流程
        if self.choice != "x":
            # 为指定场次预订座位
            self.choose_seat()
        # 打印结束语
        self.bye()

    # 为指定场次预订座位
    def choose_film(self):
        selector = FilmSelector()
        selector.display_options(self.films)
        self.choice = selector.get_choice(self.films)
    def choose_seat(self):
        # 获取用户所选择的电影
        film = self.films[int(self.choice) - 1]
        name = film['name']
        seats_list = film['seats']
        symbol = film['symbol']

        # 打印提示信息和电影宣传画
        print('正在为您预订电影《{}》的座位...'.format(name))
        print(symbol)
        time.sleep(0.2)

        # 实例化 SeatBooking 类
        booking = SeatBooking()
        # 打印所有座位的预订信息
        booking.check_bookings(seats_list)
        # 按用户输入的座位号预订座位
        booking.book_seat(seats_list)

    def welcome(self):
        print('+============================+')
        print('+     欢迎来到时光电影院     +')
        print('+============================+')
        print('')
        time.sleep(0.7)
    def bye(self):
        print('')
        time.sleep(0.2)
        print('+============================+')
        print('+  已经退出系统，下次见！👋  +')
        print('+============================+')

# 实例化 Controller 类
s = Controller(infos)