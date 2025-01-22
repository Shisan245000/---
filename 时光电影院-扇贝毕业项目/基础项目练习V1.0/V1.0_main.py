# _*_ coding:utf-8 _*_
# 开发人员：Asa
# 开发时间：2025-01-2015:19
# 文件名:main.py
# 开发工具:PyCharm
# ...
# ...
#导入SeatsBooking类
from SeatBooking import SeatBooking
import infos

seat_list = infos.infos[0]["seats"]
#实例化 SeatBooking 类
booking = SeatBooking()
# 打印所有座位的预订信息
booking.check_bookings(seat_list)
# 按用户输入的座位号预订座位
booking.book_seat(seat_list)
