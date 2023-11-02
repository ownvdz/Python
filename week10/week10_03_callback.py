# 2023-11-02

def call_10_times(func) :
    for i in range(10) :
        func(i)

def print_hello(i) :
    print(f"{i+1} 안녕")

call_10_times(print_hello)

# ---------------------------------------

a = ["1", "2", "3"]
a = list(map(int, a))
b = sum(a)

print(b)

def power(item) :
    return item**2

a = [1, 2, 3]
b = list(map(power, a))

print(b)

# -----------------------------------------

a = [1, 2, 3]
l = lambda x : x **2
b = list(map(l, a))

print(b)

# -----------------------------------------

a = [1, 2, 3]
b = list(map(lambda x : x **2, a))

print(b)