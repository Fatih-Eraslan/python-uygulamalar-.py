def açi_alma():

 açi1=int(input("1.açiyi girin= \n"))
 açi2=int(input("2.açiyi girin= \n"))
 açi3=int(input("3.açiyi girin= \n"))

 return (açi1,açi2,açi3,)

def açi_kontrol(açi1,açi2,açi3):
 
 if (açi1==açi2==açi3):
    print("bu bir eşkenar üçgendir.")
 elif (açi1==açi2):
    print("bu bir ikizkenar üçgendir.")
 else:
    print("bu bir çeşit kenar üçgen değildir.")
açi_değer = açi_alma()
açi_kontrol(açi_değer[0],açi_değer[1],açi_değer[2])

