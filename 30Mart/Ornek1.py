a = " hello world"
print("Reverse is", a[::-1])  # Metni ters cevirme

n = 10
result = 1 < n < 20
print(result)
result = 1 > n <= 9
print(result)


def x():
    return 1, 2, 3, 4


a, b, c, d = x()
print(a, b, c, d)

count = 4
print("Geeksforgeek\n" * count)  # count times print

print(any(a % 2 == 0 for a in range(0, 10, 2)))
print(all(a % 2 == 0 for a in range(0, 10, 2)))

for a in range(0, 10, 2):
    print(a)


def greet_user():
    """Display a simple greeting"""
    print("Hello")


greet_user()

