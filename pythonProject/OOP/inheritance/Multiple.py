class Parent1:
    def assign_string_one(self, str1):
        self.str1 = str1

    def show_parent1(self):
        return self.str1


class Parent2:
    def assign_string_two(self, str2):
        self.str2 = str2

    def show_parent2(self):
        return  self.str2
class Child (Parent1, Parent2):
    def assign_string_three(self, str3):
        self.str3=str3

    def show_string_three(self):
        return self.str3

c = Child()
c.assign_string_one("one")
c.assign_string_two("two")
c.assign_string_three("three")
print(c.show_parent1())
print(c.show_parent2())
print(c.show_string_three())