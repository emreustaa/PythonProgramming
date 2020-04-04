class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting")

    def roll_over(self):
        print(self.name.title() + " rolled over!")


myDog = Dog("Karabas", 5)
print("My dog is " + myDog.name.title() + ".")
print("My dog is " + str(myDog.age) + " years old")
myDog.sit()
myDog.roll_over()

print("")
yourdog = Dog("Lucy", 10)
print("Your dog is " + yourdog.name.title() + ".")
print("Your dog is " + str(yourdog.age) + " years old")
yourdog.sit()
yourdog.roll_over()
