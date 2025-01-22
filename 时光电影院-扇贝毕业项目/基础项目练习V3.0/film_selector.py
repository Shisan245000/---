# _*_ coding:utf-8 _*_
# 开发人员：Asa
# 开发时间：2025-01-2016:06
# 文件名:film_selector.py
# 开发工具:PyCharm
# ...
# ...
import time
from infos import infos

class FilmSelector:
    def display_options(self,films):
        print("今日影院排片列表：")
        print('+================+')
        # 按行打印每部电影
        for i in range(len(films)):
            print('{} - {}'.format(i + 1, films[i]['name']))
            time.sleep(0.2)
        # 打印退出选项
        print('x - 退出')
        print('+================+')
        time.sleep(0.7)

    def get_choice(self, films):
        # 符合要求的输入列表
        valid_choice = [str(i + 1) for i in range(len(films))]
        valid_choice.append('x')

        choice = input("你的选择是？")
        # 当不符合要求时，循环获取新的选项
        while choice not in valid_choice:
            choice = input("没有按照要求输入哦，请重新输入")
            # 返回用户做出的选择
        return choice
        #print(choice)

# choice = FilmSelector()
# choice.display_options(infos)
# print(type(choice.get_choice(infos)))
