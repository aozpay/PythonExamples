from kutuphane import *



print("""**********************************

KUTUPHANE V.0 HOSGELDİNİZ.

İŞLEM SECİNİZ ; 

1-> KITAPLARI GOSTER

2-> KITAP SORGULAMA

3-> KITAP EKLE

4-> KITAP SIL

5-> BASKI YUKSELT


CIKIS YAPMAK ICIN q'YA BASINIZ.
""")

kutuphane = Kütüphane()


while True:
    islem = input("Secim yapiniz..")
    if(islem == "q"):
        print("Cikis yapiliyor..")
        break
    elif(islem == "1"):
        kutuphane.kitapları_goster()
    elif(islem == "2"):
        isim = input("Hangi kitabi istiyorsunuz ? ")
        print("Kitap sorgulaniyor")
        time.sleep(2)
        kutuphane.kitap_sorgula(isim)
    elif(islem == "3"):
        isim = input("Kitap ismini giriniz")
        yazar = input("Kitap yazarini giriniz")
        yayinevi = input("Kitabın yayinevini giriniz..")
        tür = input("Kitabın türünü giriniz..")
        baskı = input("Baskı giriniz .. ")
        yeni_kitap = Kitap(isim,yazar,yayinevi,tür,baskı)

        print("Kitap ekleniyor..")
        time.sleep(2)
        kutuphane.kitap_ekle(yeni_kitap)
        print("kitap eklendi..")
    elif(islem == "4"):
        isim = input("Hangi kitabı silmek istiyorsunuz ? ")
        time.sleep(2)
        cevap = input("Emin misiniz ??  E\H")
        if(cevap == "E"):
            print("Kitap siliniyor.")
            time.sleep(2)
            kutuphane.kitap_sil(isim)
            time.sleep(2)
            print("Kitap silindi.")


    elif(islem == "5"):
        isim = input("Hangi kitabin baskini yükseltmek istiyorsunuz ?")
        print("Baskı yükseltiliyor..")
        time.sleep(2)
        kutuphane.baskı_yükselt(isim)
        time.sleep(2)
        print("Baskı yükseltildi.")
    else:
        print("Hatalı giris yaptiniz")

