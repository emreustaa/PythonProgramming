numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
girilen = int(input("Enter a number : "))
big = []
least = []

while numbers:
    pop = numbers.pop()
    if girilen > pop:
        big.append(pop)
    else:
        least.append(pop)
print(big)
print(least)
