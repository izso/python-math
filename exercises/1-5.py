#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 分数の計算をするプログラム
"""
Run until exit layout
"""

def multi_table(a):
    for i in range(1,11):
        print('{0} x {1} = {2}'.format(a,i,a*i))

if __name__ == "__main__":
    while True:
        try:
            a = float(input("Enter a number: "))
        except:
            print("please input number")
            continue
        multi_table(a)
        answer = input('Do you want to exit?(y) for yes ')
        if answer == "y":
            break

"""
他のプログラムも全部直すのは面倒臭いので割愛
"""

