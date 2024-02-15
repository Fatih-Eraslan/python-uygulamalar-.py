import math

while True:
    def squareroot(a):
     result=math.sqrt(a)
     print(result)
     
    a=float(input("birinci sayiyi giriniz: \n"))
    process=str(input("yapacağınız işlemi seçiniz: +,-,*,/,**,k,q \n"))

    if process=="q":
        print("hoşçakalın")
        break
    elif process=="k":
        squareroot(a)
        continue
    b=float(input("ikinci sayiyi giriniz: \n"))

    def add(a,b):
        result=a+b
        print(result)

    def minus(a,b):
       result=a-b
       print(result)

    def impact(a,b):
       result=a*b
       print(result)

    def divide(a,b):
       result=a/b
       print(result)

    def exponentiation(a,b):
       result=a**b
       print(result)
        
    if process=="+":
       add(a,b)
    elif process=="-":
       minus(a,b)
    elif process=="*":
       impact(a,b)
    elif process=="/":
       divide(a,b)
    elif process=="**":
       exponentiation(a,b)

"Bu işlemde python da kullanılan hesap makinesi kodlarını verdim."
*Umarım faydalı olmuşumdur :) *

       
