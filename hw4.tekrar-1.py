def enter_product():
    product1=int(input("1. ürünü giriniz: \n"))
    product2=int(input("2. ürünü giriniz: \n"))
    total=product1+product2
    return (total)

def product_control(total):
    if total<=200:
        print("ödenecek miktar: ",total)

    elif total>=200:
        discount=total*(0.25)
        total=