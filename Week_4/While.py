n = 1

while (n <= 5):
    print(n)
    n += 1

girilen = "Tell me something and I will repeat it back to you:"
girilen += "\nEnter 'quit' to end program "

active = True
while active:
    message = input(girilen)

    if message == 'quit':
        active = False
    else:
        active = True
print("Program sonlandı! Durum :", active)

unconfirmed_users = ['alice', 'brian', 'candice']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying users : " + current_user.title())
    confirmed_users.append(current_user)

for confirmed_users in confirmed_users:
    print(confirmed_users.title())

