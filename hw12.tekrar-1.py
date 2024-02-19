ağirlik=int(input("ağirliğinizi girin= "))
boy=int(input("boyunuzu girin="))
VKİ=(ağirlik/boy*boy)

if (VKİ>=18  <=25):
   print("Normal")
elif (VKİ>=25 <=30):
   print("kilolu")
elif (VKİ >=30 <=35):
   print("OBEZ")
elif VKİ>=35:
   print("CİDDİ OBEZ")