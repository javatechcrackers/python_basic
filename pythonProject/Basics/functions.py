def run():
    print("RUN")


def walk(x):
    print("WALK " + x)

def talk(x, y):
    print(f"value of x is {x} and value of y is {y}")

def talk1(*args):
    print(f"value of x is {args[0]} and value of y is {args[1]}")

def multipleFunction(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))

run()
walk('10 km')
talk(y=10,x=20)
talk1(5,2)
multipleFunction(firstArg='Javat', Second='Point', Third='Ayush',Fourth = 6000)

g = lambda x: x*x*x
print(g(7))

#lambda with filter

l1 = [2,4,3,7,5,6,9,10]
l2 = list(filter(lambda x: (x%2!=0), l1))

print(l2)


#lambda with map
l3 = [2,4,3,7,5,6,9,10]
l4 = list(map(lambda x: x*2, l3))

print(l4)

#lambda with reduce
from functools import reduce

sum=reduce(lambda x,y: x+y,l4)
print(sum)