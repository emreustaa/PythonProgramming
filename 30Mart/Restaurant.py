class Restaurant():
    def __init__(self, resturant_name, cuisine_type):
        self.resturant_name = resturant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.resturant_name + " serves wonderful " + self.cuisine_type + ".")

    def open_restaureant(self):
        print(self.resturant_name + " is open. Come on in!")


restaurant = Restaurant("the mean queen", "pizza")
# print(restaurant.resturant_name)
# print(restaurant.cuisine_type)
restaurant.describe_restaurant()
# restaurant.open_restaureant()

secRes = Restaurant("ludvig's bistro", "seafood")
secRes.describe_restaurant()

thirdRes = Restaurant("mango thai", "thai food")
thirdRes.describe_restaurant()
