counter = 1
dictionary = {}
while counter < 6:
    isim = input("What is your name?:")
    language = input("Which programming language is your favourite?:")
    dictionary[isim] = language
    counter += 1
print("")
print("--- Results ---")
for k, v in dictionary.items():
    print(k.title() + "'s favourite programming language is " + v.title() +".")
