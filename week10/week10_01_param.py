# 2023-11-02

def intro (name, grade, *hobbies) :
    print(type(hobbies))
    print(name, grade)
    if 0 < len(hobbies) :
        print(", ".join(hobbies))
    else :
        print(hobbies)
        print("없다")

intro("홍길동", 1, "A", "B", "C", "D")
intro("홍길동", 1, "A")
intro("홍길동", 1)

def intro (name, grade = 1, hobby = "없음") :
    print(f"이름 : {name}")
    print(f"학년 : {grade}")
    print(f"취미 : {hobby}")

# intro(hobby = "게임", grade = 2)      <- 잘못됨
# intro(hobby = "게임", name = "홍길동")
# intro(name = "홍길동", hobby = "게임")
# intro("홍길동", hobby = "게임")
# intro("홍길동", "없다")
# intro("홍길동")

# 기본값 매개변수 선언은 뒤쪽에
# def intro (grade=1, name) :                       <- 잘못됨
#     print(f"나는 {name}이고, {grade}학년이야")     <-
#
# def intro (hobby, grade=1, name) :
#     print(f"나는 {name}이고, {grade}학년이야")

def intro (name, grade=1) :
    print(f"나는 {name}이고, {grade}학년이야")

# intro("홍길동")
# intro("홍길동", 3)

# print("홍길동", end="\t")
# print("20", "인하", "공업", sep="\n")