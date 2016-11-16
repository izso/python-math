#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 単位変換プログラムの拡張
"""
km <-> mile
kg <-> pond
"""


def print_nemu():
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Kilograms to Ponds")
    print("4. Ponds to Kilograms")


def km_miles():
    km = float(input('Enter distance in kilometers : '))
    miles = km / 1.609
    print('Distance is {0} miles'.format(miles))


def miles_km():
    km = float(input('Enter distance in miles : '))
    miles = km * 1.609
    print('Distance is {0} miles'.format(miles))


def kg_ponds():
    km = float(input('Enter weight in kilograms : '))
    miles = km / 0.453
    print('Distance is {0} ponds'.format(miles))


def ponds_km():
    km = float(input('Enter weight in ponds : '))
    miles = km * 0.453
    print('Distance is {0} kilograms'.format(miles))

if __name__ == "__main__":
    print_nemu()
    choice = input("Whitch conversioin would you like to do? : ")
    if choice == "1":
        km_miles()
    if choice == "2":
        miles_km()
    if choice == "3":
        kg_ponds()
    if choice == "4":
        ponds_km()
