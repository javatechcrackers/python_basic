a = 10
b = 10

if a > b:
    print("a is greater than b")
elif b > a:
    print("b is greater than a")
else:
    print("both are eqauls")

x = 10
y = 20
z = 30

if (x > y) & (y > z):
    print("x is greatest")
elif (y > x) & (y > z):
    print("y is greatest")
else:
    print("z is greatest")

#if with tuple
tup1 = {'a','b','c'}

if 'a' in tup1:
    print("a is present")
else:
    print("a is not present")

#if with list
l1 = ['a', 'b', 'c']
if l1[1] == 'b':
    l1[1] = 'k'
print(l1)

#if with dictionary
d1 = {"k1":10,"k2":20,"k3":30}
if d1['k3'] == 30:
    d1['k3'] = d1['k3'] + 100

print(d1)