class Phone1:
    def set_color(self, color):
        self.color = color

    def set_cost(self, cost):
        self.cost = cost

    def show_color(self):
        return self.color
    def show_cost(self):
        return self.cost

p2= Phone1()
p2.set_color("blue")
p2.set_cost(5000)

print(p2.show_color())
print(p2.show_cost())