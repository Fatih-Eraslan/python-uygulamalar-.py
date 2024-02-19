def enter_weather():
 hava_derecesi=int(input("hava derecesi girin= "))
 return hava_derecesi

def weather_control(hava_derecesi):
 if hava_derecesi<=5:
    print("hava soğuk")
 elif hava_derecesi>=6 and hava_derecesi<=14:
    print("hava ilik")
 elif hava_derecesi>=15:
    print("hava sicak")
    
 