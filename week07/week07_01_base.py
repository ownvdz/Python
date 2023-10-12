# 2023-10-12

def test():
    print(1)
    print(2)
    # return None <--- 자동적으로 붙음

print(test())   # None

def test():
    print("3")
    print("4")
    return 0

print(test())   # 0

def test():
    print("5")
    return      # 함수를 끝냄
    print("6")

print(test())   # None

def test(itr):  # itr <--- '매개변수(parameter)'
    for i in range(itr):
        print("안녕")
    

print(test(2))  # 2 <--- '인자', 'argument'

def test(i, string):
    for it in range(i):
        print(string)
    
test(2, "안녕")


def avg(arr):
    if type(arr) is list:
        return sum(arr)/len(arr)



print(avg([1, 2, 3, 4]))
result = avg("1234")
if result:
    print(result)
else:
    print("자료에 문제가 있습니다")
