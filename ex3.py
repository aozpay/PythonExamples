# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 17:47:50 2018

@author: alican
"""


secim = int(input("Ücgen mi yoksa dörtgen ile mi çalışacaksınız ? \n Ücgen için -> 1 \n dörtgen için -> 2 \n"))
if (secim == 1 ):
    print("Ücgen secimi yaptiniz.")
    birincikenar = float(input("Birinci kenarin uzunluğunu giriniz."))
    ikincikenar = float(input("İkinci kenarin uzunluğunu giriniz."))
    ücüncükenar = float(input("Ücüncü kenarin uzunluğunu giriniz."))
    if(abs(birincikenar-ikincikenar)<ücüncükenar<abs(birincikenar+ikincikenar) or abs(birincikenar-ücüncükenar)<ikincikenar<abs(birincikenar+ücüncükenar) or abs(ikincikenar-ücüncükenar)<birincikenar<abs(ikincikenar+ücüncükenar) ):
        print("Ücgeniniz oluşabilir.")
        if(birincikenar == ikincikenar and ikincikenar != ücüncükenar  or birincikenar == ücüncükenar and ücüncükenar!=ikincikenar or ikincikenar == ücüncükenar and ücüncükenar != birincikenar):
            print("Ücgenininz ikizkenardir.")
        elif(birincikenar == ikincikenar and ikincikenar == ücüncükenar ):
            print("Ücgenininz esitkenardir.")
        else:
            print("Ücgenininz normal bir üçgendir.")
    else:
        print("ücgenininz oluşmayacaktır.")
if (secim == 2):
    print("Dörtgen seçimi yaptınız.")
    birincikenar = float(input("Birinci kenarin uzunluğunu giriniz."))
    ikincikenar = float(input("İkinci kenarin uzunluğunu giriniz."))
    ücüncükenar = float(input("Ücüncü kenarin uzunluğunu giriniz."))     
    dördüncükenar = float(input("Dördüncü kenarin uzunluğunu giriniz."))
    if(birincikenar == ikincikenar and ikincikenar == ücüncükenar and ücüncükenar == dördüncükenar):
        print("Girdiginiz dörtgen karedir.")
    if(birincikenar == ücüncükenar and ücüncükenar != ikincikenar and ücüncükenar != dördüncükenar):
         print("Girdiginiz dörtgen dikdörtgendir.")