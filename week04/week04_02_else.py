# 2023-09-21

number = int(input("정수:"))

if number > 0:
    print("양수")
elif number < 0:
    print("음수")
else:
    print("0")


# if number > 0:
#     print("양수")
# else:
#     print("음수 or 0")


reg_number = input("주민등록번호")
gender_number = int(reg_number[6])

if gender_number % 2 == 1:
    print("남자")
else:
    print("여자")