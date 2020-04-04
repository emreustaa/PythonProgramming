class Person():
    def __init__(self, name, surname,
                 year_of_work, salary):
        self.name = name
        self.surname = surname
        self.year_of_work = year_of_work
        self.salary = salary

    def printInfo(self):
        return "Called printInfo Method...\n" + "Name: " + self.name + ", " + "Surname: " + self.surname + ", " \
               + "Year of Work: " + str(self.year_of_work) + ", " + "Salary: " + str(self.salary)

    def raiseSalary(self, raise_amount):
        self.salary = self.salary + (self.salary * raise_amount)
        print("Called raiseSalary Method... Given Parameter: " + str(raise_amount))


person_1 = Person("Ali", "Yılmaz", 5, 3500)
person_2 = Person("Ayşe", "Yılmaz", 6, 4270)

person_1.raiseSalary(0.10)
print(person_1.printInfo())
print("-----")
person_2.raiseSalary(0.25)
print(person_2.printInfo())
