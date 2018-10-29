#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:    Jack
@datetime:  2018/8/30 14:10
@E-mail:    zhangxianlei117@gmail.com
"""

roman_map = {
    'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9,
    'X': 10, 'XX': 20, 'XXX': 30, 'XL': 40, 'L': 50, 'LX': 60, 'LXX': 70, 'LXXX': 80, 'XC': 90,
    'C': 100, 'CC': 200, 'CCC': 300, 'CD': 400, 'D': 500, 'DC': 600, 'DCC': 700, 'DCCC': 800, 'CM': 900,
    'M': 1000, 'MM': 2000, 'MMM': 3000
}


def romanToInt(s):
    unit = ''
    unit_sum = 0
    total = 0
    for letter in s:
        unit += letter
        if roman_map.has_key(unit):
            unit_sum = roman_map[unit]
        else:
            unit = letter
            total += unit_sum
            unit_sum = roman_map[unit]
    return total + unit_sum


if __name__ == '__main__':
    print romanToInt('XVI')