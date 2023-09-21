# 2023-09-21

reg_number = input("주민등록번호")
gender_number = int(reg_number[6])

if gender_number % 2 == 1:
    print("남자")

if gender_number == 1 or gender_number == 3 or gender_number == 5 or gender_number == 7:
    print("남자")

# if gender_number in "1357":
#     print("남자")

if str(gender_number) in "1357":
    print("남자")


print("--------------------------------------")


number = int(input("정수:"))
if number > 0:
    print("양수")

if number < 0:
    print("음수")

if number == 0:
    print("0")
