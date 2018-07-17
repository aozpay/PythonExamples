# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 17:36:13 2018

@author: alican
"""

sayi1 = int(input("Birinci sayiyi giriniz"))
sayi2 = int(input("İkinci sayiyi giriniz"))
print("Sayilar degistirilmeden önce = sayi1 : {} , sayi2 : {}".format(sayi1,sayi2))
sayi1,sayi2 = sayi2,sayi1
print("Sayilar degistirildikten sonra = sayi1: {} , sayi2 : {}".format(sayi1,sayi2))