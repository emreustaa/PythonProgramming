class Material:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def decreaseStock(self, sellCount):
        if (self.stock - sellCount) > 0:
            self.stock = self.stock - sellCount
        else:
            print("There is not enough Hammer.")

    def printValue(self):
        print(self.stock)


class Factory:
    def __init__(self, name):
        self.name = name
        self.materialList = []

    def addMaterial(self, material):
        self.materialList.append(material)

    def removeMaterial(self, material):
        self.materialList.remove(material)

    def sellMaterial(self, material, amount):
        if material in self.materialList:
            material.decreaseStock(amount)

    def printMaterialList(self):
        for material in self.materialList:
            print("Title: " + material.name + ", " + "Price: " + str(material.price) + ", " + "Stock: " + str(material.stock))


material_1 = Material("Hammer", 25, 5)
material_2 = Material("Brush", 3, 2)
material_3 = Material("Nothing", 100, 5)

factory = Factory("Factory")

factory.addMaterial(material_1)
factory.addMaterial(material_2)
factory.addMaterial(material_3)

factory.removeMaterial(material_3)

factory.sellMaterial(material_1, 6)
factory.sellMaterial(material_2, 1)

factory.printMaterialList()
