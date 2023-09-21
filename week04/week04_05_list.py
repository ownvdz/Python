# 2023-09-21

test = ["딸기", "포도", "수박", "참외", "멜론"]

del test[4]
print(test)

del test[0:2]
print(test)

test.append("키위")
test.append("복숭아")
test.append("사과")
print(test)

test.remove("수박")
print(test)

p = test.pop()
print(p)
test.pop()
test.pop()
test.pop(0)
print(test)