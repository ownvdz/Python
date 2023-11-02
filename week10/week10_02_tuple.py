# 2023-11-02

tuple_data = (10, 20, 30)
a = tuple_data[0]
b = tuple_data[:]
print(a, b, list(b))

for i, v in enumerate(tuple_data) :
    print(i, v)

a = []
b = [1]
c = ()
# d = (1)   <- tuple이 아니라 int
d = (1,)

print(type(a), type(b), type(c), type(d))

a, b = [10, 20]
c, d = (10, 20)

print(a, b, c, d)

a = 10, 20, 30
b, c, d = a

print(a, b, c, d)

a, b = 10, 20
b, a = a, b

print(a, b)

for a in enumerate([1,2,3]) :
    print(a[0], b[1])

for i, v in enumerate([1,2,3]) :
    print(i, v)

def divide(n1, n2) :
    return n1 // n2, n1 % n2    # tuple     (n1//n2, n1%n2)

q, r = divide(10, 3)
print(q, r)

