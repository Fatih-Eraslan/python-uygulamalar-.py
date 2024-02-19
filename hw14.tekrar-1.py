sayi1=int(input("1.sayiyi giriniz= "))
sayi2=int(input("2.sayiyi giriniz= "))
sayi3=int(input("3.sayiyi giriniz= "))

if sayi1>=sayi2 and sayi1>=sayi3:
    büyük_sayi=sayi1
    print("büyük sayi=",büyük_sayi)
elif sayi2>=sayi1 and sayi2>=sayi3:
    büyük_sayi=sayi2
    print("büyük sayi=",büyük_sayi)
else:
    büyük_sayi=sayi3
    print("büyük sayi=",büyük_sayi)