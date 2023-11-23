# 2023-11-23
import student as st
# from student import Student1

# step1
print("step1", "-" * 10)
stu1 = st.Student1()
print(stu1)

# step2
print("step2", "-" * 10)
stu1 = st.Student2()
print(stu1)

stu2 = st.Student2()
print(stu2)
# print(stu2.name)

# step3
print("step3", "-" * 10)
stu3 = st.Student3()
print(stu3)
print(stu3.name)
print(stu3.number)
print(stu3.major)

# step4
print("step4", "-" * 10)
stu4 = st.Student4("김인하", "20230001", "컴퓨터정보")
print(stu4)
print(stu4.name)
print(stu4.number)
print(stu4.major)

stu4 = st.Student4("김인하", "20230001")
print(stu4)
print(stu4.name)
print(stu4.number)
print(stu4.major)

stu_list = []
while True:
    number = input("학번:")
    name = input("이름:")
    major = input("전공:")

    stu_list.append(st.Student4(name, number, major))
    if "Y" != input("계속할래?(y)").upper():
        break

for stu in stu_list:
    print(stu)