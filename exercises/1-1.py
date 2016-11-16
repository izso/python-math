#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("数字を入力 : ", end="")
n_str = input()

try:
        # 奇数偶数判定
    n = int(n_str)
    if (n/2).is_integer():
        print("偶数")
    else:
        print("奇数")
except:
    print("整数として認識できません。")

# ９つの数字を表示
out_str = ""
for i in range(9):
    out_str += (str(n+i*2)+",")
print(out_str[:-1])
