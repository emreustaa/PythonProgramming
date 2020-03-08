sayi = 0
while True:
    girilen = input("How old are you?:")
    if girilen == "quit":
        break
    elif int(girilen) < 3:
        print("--You get in free!")
    elif int(girilen) <=12:
        print("--Your ticket is £10.")
        sayi += 10
    else:
        print("--Your ticket is £15.")
        sayi += 15
print("Sum of All Tickets:", sayi)
