def enter_weight():

 luggage_weight=int(input("Bagaj ağirliğini giriniz: \n"))
 print("------------------------")
 return (luggage_weight)

def weight_control(luggage_weight):
 if (luggage_weight>=20):
    print("ücret ödemelisiniz.")
 else:
    print("ücret ödemeniz gerekmiyor.") 

luggage_weight = enter_weight()
weight_control(luggage_weight)