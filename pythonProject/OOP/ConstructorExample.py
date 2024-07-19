class Employee():

    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

    def show_details(self):
        print("Name - ", self.name),
        print("age - ", self.age),
        print("salary - ", self.salary)

e2 = Employee('RAJ', 22, 343434)

e2.show_details()
