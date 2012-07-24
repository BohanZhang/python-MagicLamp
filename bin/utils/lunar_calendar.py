#!/usr/bin/env python
#coding=utf-8

# 存储1901-2099年每年每月的天数，第1位到第13位存储每月（包括闰月共13月）的天数，为1表示该月为30天，
# 为0表示该月为29天。第12－15位表示该年闰月的月份，如果为0x0F表示该年没有闰月。
g_lunar_month_days = [
    0xF0EA4, 0xF1D4A, 0x52C94, 0xF0C96, 0xF1536, 0x42AAC, 0xF0AD4, 0xF16B2, 0x22EA4, 0xF0EA4,  # 1901-1910
    0x6364A, 0xF164A, 0xF1496, 0x52956, 0xF055A, 0xF0AD6, 0x216D2, 0xF1B52, 0x73B24, 0xF1D24,  # 1911-1920
    0xF1A4A, 0x5349A, 0xF14AC, 0xF056C, 0x42B6A, 0xF0DA8, 0xF1D52, 0x23D24, 0xF1D24, 0x61A4C,  # 1921-1930
    0xF0A56, 0xF14AE, 0x5256C, 0xF16B4, 0xF0DA8, 0x31D92, 0xF0E92, 0x72D26, 0xF1526, 0xF0A56,  # 1931-1940
    0x614B6, 0xF155A, 0xF0AD4, 0x436AA, 0xF1748, 0xF1692, 0x23526, 0xF152A, 0x72A5A, 0xF0A6C,  # 1941-1950
    0xF155A, 0x52B54, 0xF0B64, 0xF1B4A, 0x33A94, 0xF1A94, 0x8152A, 0xF152E, 0xF0AAC, 0x6156A,  # 1951-1960
    0xF15AA, 0xF0DA4, 0x41D4A, 0xF1D4A, 0xF0C94, 0x3192E, 0xF1536, 0x72AB4, 0xF0AD4, 0xF16D2,  # 1961-1970
    0x52EA4, 0xF16A4, 0xF164A, 0x42C96, 0xF1496, 0x82956, 0xF055A, 0xF0ADA, 0x616D2, 0xF1B52,  # 1971-1980
    0xF1B24, 0x43A4A, 0xF1A4A, 0xA349A, 0xF14AC, 0xF056C, 0x60B6A, 0xF0DAA, 0xF1D92, 0x53D24,  # 1981-1990
    0xF1D24, 0xF1A4C, 0x314AC, 0xF14AE, 0x829AC, 0xF06B4, 0xF0DAA, 0x52D92, 0xF0E92, 0xF0D26,  # 1991-2000
    0x42A56, 0xF0A56, 0xF14B6, 0x22AB4, 0xF0AD4, 0x736AA, 0xF1748, 0xF1692, 0x53526, 0xF152A,  # 2001-2010
    0xF0A5A, 0x4155A, 0xF156A, 0x92B54, 0xF0BA4, 0xF1B4A, 0x63A94, 0xF1A94, 0xF192A, 0x42A5C,  # 2011-2020
    0xF0AAC, 0xF156A, 0x22B64, 0xF0DA4, 0x61D52, 0xF0E4A, 0xF0C96, 0x5192E, 0xF1956, 0xF0AB4,  # 2021-2030
    0x315AC, 0xF16D2, 0xB2EA4, 0xF16A4, 0xF164A, 0x63496, 0xF1496, 0xF0956, 0x50AB6, 0xF0B5A,  # 2031-2040
    0xF16D4, 0x236A4, 0xF1B24, 0x73A4A, 0xF1A4A, 0xF14AA, 0x5295A, 0xF096C, 0xF0B6A, 0x31B54,  # 2041-2050
    0xF1D92, 0x83D24, 0xF1D24, 0xF1A4C, 0x614AC, 0xF14AE, 0xF09AC, 0x40DAA, 0xF0EAA, 0xF0E92,  # 2051-2060
    0x31D26, 0xF0D26, 0x72A56, 0xF0A56, 0xF14B6, 0x52AB4, 0xF0AD4, 0xF16CA, 0x42E94, 0xF1694,  # 2061-2070
    0x8352A, 0xF152A, 0xF0A5A, 0x6155A, 0xF156A, 0xF0B54, 0x4174A, 0xF1B4A, 0xF1A94, 0x3392A,  # 2071-2080
    0xF192C, 0x7329C, 0xF0AAC, 0xF156A, 0x52B64, 0xF0DA4, 0xF1D4A, 0x41C94, 0xF0C96, 0x8192E,  # 2081-2090
    0xF0956, 0xF0AB6, 0x615AC, 0xF16D4, 0xF0EA4, 0x42E4A, 0xF164A, 0xF1516, 0x22936,           # 2090-2099
]

import sys
from datetime import datetime, timedelta

START_YEAR, END_YEAR = 1901, 1900 + len(g_lunar_month_days)
LUNAR_START_DATE, SOLAR_START_DATE = (1901, 1, 1), datetime(1901,2,19) # 1901年正月初一的公历日期为1901/2/19
LUNAR_END_DATE, SOLAR_END_DATE = (2099, 12, 30), datetime(2100,2,18) # 2099年12月30的公历日期是2100/2/8

def date_diff(tm):
    return (tm - SOLAR_START_DATE).days

def get_leap_month(lunar_year):
    return (g_lunar_month_days[lunar_year-START_YEAR] >> 16) & 0x0F

def lunar_month_days(lunar_year, lunar_month):
    return 29 + ((g_lunar_month_days[lunar_year-START_YEAR] >> lunar_month) & 0x01)

def lunar_year_days(year):
    days = 0
    months_day = g_lunar_month_days[year - START_YEAR] 
    for i in range(1, 13 if get_leap_month(year) == 0x0F else 14):
       day = 29 + ((months_day>>i)&0x01)
       days += day
    return days

# 根据公历计算农历日期，返回(year,month,day,isLeap)
def get_lunar_date(tm):
    if (tm < SOLAR_START_DATE or tm > SOLAR_END_DATE):
        raise Exception('out of range')

    span_days = date_diff(tm)

    year, month, day = START_YEAR, 1, 1
    tmp = lunar_year_days(year)
    while span_days >= tmp:
        span_days -= tmp
        year += 1
        tmp = lunar_year_days(year)

    leap = False
    tmp = lunar_month_days(year, month)
    while span_days >= tmp:
        span_days -= tmp
        month += 1
        tmp = lunar_month_days(year, month)
    leap_month = get_leap_month(year)
    if  month > leap_month:
        month -= 1
        if month == leap_month:
            leap = True

    day += span_days
    return (year, month, day, leap)

# 根据农历计算公历日期，返回一个数组[datetime1, datetime2]，如果为闰月，则可能包含两个日期，否则只有一个
def get_solar_date(year, month, day):
    if not(START_YEAR<=year<=END_YEAR and 1<=month<=12 and 1<=day<=30):
        raise Exception('out of range')
    span_days = 0;
    for y in range(START_YEAR, year):
        span_days += lunar_year_days(y)
    leap_month = get_leap_month(year)
    for m in range(1, month + (month > leap_month)):
        span_days += lunar_month_days(year, m)
    span_days += day - 1
    
    if leap_month == month:
        return [SOLAR_START_DATE + timedelta(span_days), SOLAR_START_DATE + timedelta(span_days + lunar_month_days(year, leap_month))]
    else:
        return [SOLAR_START_DATE + timedelta(span_days)]

if __name__ == '__main__':
    print get_lunar_date(datetime(2012,5,22))
    
