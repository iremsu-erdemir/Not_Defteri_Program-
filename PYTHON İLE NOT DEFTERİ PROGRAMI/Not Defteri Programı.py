import os, sys, time, msvcrt

def ekleme():
    nt = input("Eklemek istediginiz notu giriniz : ")
    with open("notlar.txt","a") as f:
        f.write(nt + "\n")

def silme():
    num = int(input("Silmek istediginiz notun numarasını giriniz : "))
    with open("notlar.txt") as f:
        liste = f.readlines()
    try:
        liste.pop(num-1)
        with open("notlar.txt","w") as f:
            f.writelines(liste)
    except IndexError:
        print("Silmek için verdiğiniz not numarası hatalı")
        time.sleep(2) # ekran temizlenmeden önce 2 sn bekler
        
def listeleme():
    print("NOTLARINIZ : ")
    try:
        with open("notlar.txt") as f:
            i = 1
            for satır in f:
                print(i, '-', satır, end='')
                i = i + 1
    except FileNotFoundError: # veya OSError:
        print("notlar.txt dosyası bununamadı yeni yaratıldı")
        f = open("notlar.txt","w")
        f.close()
        
while True:
    if "idlelib" in sys.modules:  # IDLE'da çalışıyorsak input() kullanmalıyız 
        listeleme()
        print("\nNot eklemek için 1’e, Not silmek için 2’ye, Çıkış için 3’e basın")
        secim = input()
        if secim == '1':
            ekleme()
        elif secim == '2':
            silme()
        elif secim == '3':
            break
    else:  # IDLE'da değil de siyah ekranda (console) isek CLS ve getch() kullanabiliriz
        os.system("CLS")
        listeleme()
        print("\nNot eklemek için 1’e, Not silmek için 2’ye, Çıkış için ESC’ye basın")
        secim = msvcrt.getch()
        if secim == b'1':
            ekleme()
        elif secim == b'2':
            silme()
        elif secim == b'\x1b': # ESC
            break
""" Kendim 1'e basarak 'Marketten 1 kilo domates al.' notunu ekledim.Klasörün içindeki notlar dosyasında görebilirsiniz"""
