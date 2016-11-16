#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 分数の計算をするプログラム
"""
fractions_operations
"""

from fractions import Fraction


def add(a, b):
    print("Result of Addition : {0} + {1} = {2}".format(a, b, a+b))


def sub(a, b):
    print("Result of Addition : {0} - {1} = {2}".format(a, b, a-b))


def div(a, b):
    print("Result of Addition : {0} / {1} = {2}".format(a, b, a/b))


def mul(a, b):
    print("Result of Addition : {0} * {1} = {2}".format(a, b, a*b))

if __name__ == "__main__":
    try:
        a = Fraction(input("Enter 1st fraction: "))
        b = Fraction(input("Enter 2nd fraction: "))
        op = input("Choose Operation - Add, Sub, Div, Mul: ")
        if op == "Add":
            add(a, b)
        elif op == "Sub":
            sub(a, b)
        elif op == "Div":
            div(a, b)
        elif op == "Mul":
            mul(a, b)
        else:
            print("not exist such operation")
    except:
        print("number error")
