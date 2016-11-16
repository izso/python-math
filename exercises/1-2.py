#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 乗算生成期の拡張
print("掛け算の数字を入力 : ", end="")
base_n_str = input()
print("表示する行数を入力 : ", end="")
nums_n_str = input()

try:
    base_n = float(base_n_str)
except:
    print("数値として認識できません")
try:
    nums_n = int(nums_n_str)
except:
    print("行数は整数で入力して下さい")

for i in range(nums_n):
    print("{0} × {1} = {2:.1f}".format(base_n, i, base_n*i))