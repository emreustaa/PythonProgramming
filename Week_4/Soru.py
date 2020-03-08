girilen = input("Enter the number: ")
sayi = 2
while girilen != "Bitti":

    girilen = input("Enter the number: ")
    if int(girilen) % sayi == 0:
        print(sayi)
        sayi += 1
    else:
        sayi += 1

