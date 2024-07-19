fruit = {"Apple": 100, "Mango": 200, "banana": 300}

print(fruit.keys())
print(fruit.values())

fruit["orange"] = 50

print(fruit.keys())

print(fruit)

fruit.pop('orange')
print(fruit)

fruit_summer = {"watermelon": 30, "grapes": 100}

#merge dictionary
fruit.update(fruit_summer)

print(fruit)


