# 2023-11-23
# 학생 정보 관리하는 class
# class == 자료형을 만들 때 사용하는 문법
# self 매개변수 : 호출한 당사자. 호출한 값(데이터), 호출한 인스턴스(데이터 + 기능)
# i = int(1)    <-    i는 int형 인스턴스를 가르킴

class Student1:
    pass

class Student2:
    def __init__(self):
        pass

class Student3:
    def __init__(self):
        self.name = ""
        self.number = ""
        self.major = ""

class Student4:
    def __init__(self, name, number, major=""):
        self.name = name
        self.number = number
        self.major = major

    # print() 호출시 이 메소드를 호출
    # 모든 클래스에는 __str__()이 있음
    # 재정의해서 원하는 문자열로 바꾼 것
    def __str__(self) -> str:
        return f"{self.name}/{self.number}/{self.major}"