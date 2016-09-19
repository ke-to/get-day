# -*- coding: utf-8 -*-
import datetime
import sys

import jholiday
from get_day import getDay


# ---------------------------------------------------------------------------
# 使用方法：外部ファイルとして使用する場合は "from get_day import getDay"
# ---------------------------------------------------------------------------


class getDay(object):

    def holiday_list(self, start, end):
        start_date = datetime.date(start, 1, 1)
        end_date = datetime.date(end, 1, 1)
        # 日数の計算
        date_count = end_date - start_date
        self.__dict__['count'] = date_count

        # 休日判別処理
        li = []
        li_all_holiday = []
        li_holiday = []
        li_sun_stu = []
        day = start_date
        while end_date > day:
            li.append(day)
            date_y = int(day.strftime('%Y'))
            date_m = int(day.strftime('%m'))
            date_d = int(day.strftime('%d'))
            date_str = day.strftime('%Y%m%d')
            # print jholiday.holiday_name(date_y,date_m,date_d)
            if jholiday.holiday_name(date_y, date_m, date_d):
                li_all_holiday.append(day)
                li_holiday.append(day)
            elif day.weekday() == 5 or day.weekday() == 6:
                li_all_holiday.append(day)
                li_sun_stu.append(day)
            day = day + datetime.timedelta(1)

        # print li
        print ('day: %s' % date_count)
        print ('holiday: %s' % len(li_holiday))
        print ('sun_stu: %s' % len(li_sun_stu))

        # 全日のリスト
        self.__dict__['all'] = li
        # 全休日のリスト
        self.__dict__['all_holiday'] = li_all_holiday
        # 祝日のリスト
        self.__dict__['holiday'] = li_holiday
        # 土日のリスト
        self.__dict__['sun_stu'] = li_sun_stu
        # 平日のリスト
        self.__dict__['weekday'] = set(li) - set(li_all_holiday)

if __name__ == '__main__':
    a = getDay()
    a.holiday_list(2006, 2007)
    print a.all
    print a.all_holiday
    print a.holiday
    print a.sun_stu
    print a.weekday


s = getDay()
Y = 2006
data = []
for i in range(1, 12):
    s.holiday_list(Y, Y + 1)
    cnt_day = len(s.weekday)
    data.append(cnt_day)
    Y += 1
