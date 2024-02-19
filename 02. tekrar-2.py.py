def user_angle():
 angle1=int(input("1.açiyi girin= "))
 angle2=int(input("2.açiyi girin= "))
 angle3=int(input("3.açiyi girin= "))
 return (angle1,angle2,angle3)

def angle_control(angle1,angle2,angle3):

 total=angle1+angle2+angle3
 if (total==180):
    print("Bu bir üçgendir.")
 else:
    print("Bu bir üçgen değildir.")

values = user_angle()
angle_control(values[0],values[1],values[2])