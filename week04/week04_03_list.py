# 2023-09-21
# list는 array와 비슷한 역할
# array(배열) -> 고정길이, 메모리에 연속적인 할당

stu_1 = [20230001, "김인하", "컴정", 20]
stu_2 = [20230010, "이인하", "컴시", 21]

# stu_2 성(family name) 출력
print(stu_2[1][0])

# stu_1 입학년도 출력
print(stu_1[0]//10000)
print(str(stu_1[0])[:4])

print("학번")
print(stu_1[0])
print(stu_2[0])

print("이름")
print(stu_1[1])
print(stu_2[1])

stu_1[0] = 20230002
print(stu_1[0])


test_list = list()      # 생성자
print(test_list, type(test_list))

test_list = []          # 기호로 표현
print(test_list, type(test_list))

test_list = [1, 2, 3]
print(test_list)

#다른 타입을 넣어도 됨
test_list = ["홍길동", 33, 170]
print(test_list)

for data in test_list:
    print(data)