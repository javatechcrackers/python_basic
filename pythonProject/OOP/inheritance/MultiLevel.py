class Parent:
    def get_name(self, name):
        self.name = name

    def show_name(self):
        return self.name


class Child(Parent):
    def get_age(self, age):
        self.age = age

    def show_age(self):
        return self.age


class GrandChild(Child):
    def get_gender(self, gender):
        self.gender = gender

    def show_gender(self):
        return self.gender


gc = GrandChild()
gc.get_name("prashant")
gc.get_gender("male")
gc.get_age(34)

print(gc.show_name())
print(gc.show_gender())
print(gc.show_age())
