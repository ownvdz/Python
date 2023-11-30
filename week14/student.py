import datetime as dt
import random
import os

class Student:
    time_format = "%Y-%m-%d %H:%M:%S"

    @staticmethod
    def create_obj(record):
        record = record.strip()
        fields = record.split("|")

        if len(fields) == 6:
            name = fields[0]
            num = fields[1]
            kor = int(fields[2])
            math = int(fields[3])
            eng = int(fields[4])
            regdate = dt.datetime.strptime(fields[5], Student.time_format)

            return Student(num, name, kor, math, eng, regdate)

    @classmethod
    def create_test(cls, record):
        pass

    def __init__(self, num, name, kor=0, math=0, eng=0, regdate = None) -> None:
        self.num = num
        self.name = name
        self.kor = kor
        self.math = math
        self.eng = eng

        if regdate == None:
            days = random.randrange(-2, 3)
            self.regdate = dt.datetime.now() + dt.timedelta(days= days)
        else:
            self.regdate = regdate

    def get_sum(self):
        return self.kor + self.math + self.eng
    
    def get_average(self):
        return self.get_sum()/3
    
    def __str__(self) -> str:
        average = self.get_average()
        return f"이름:{self.name} 학번:{self.num} 평균:{average:0.1f}"

    def __gt__(self, value):
        if value == isinstance(value, Student):
            return self.get_sum() > value.get_sum()
        
    def __lt__(self, value):
        if value == isinstance(value, Student):
            return self.get_sum() < value.get_sum()
        
    def __eq__(self, value):
        if value == isinstance(value, Student):
            return self.get_sum() == value.get_sum()
        
    def __ne__(self, value):
        if value == isinstance(value, Student):
            return self.get_sum() != value.get_sum()
        
    def make_record(self):
        str_time = dt.datetime.strftime(self.regdate, Student.time_format)
        return f"{self.name}|{self.num}|{self.kor}|{self.math}|{self.eng}|{str_time} \n"

if __name__ == "__main__":

    target_path = "c:\\s202344053"
    target_file = "scores.txt"
    target_full_file = os.path.join(target_path, target_file)
    print(target_full_file)

    students = []
    if os.path.exists(target_full_file):
        with open(target_full_file, "r", encoding="utf8") as file:
            for record in file:
                stu = Student.create_obj(record)
                if isinstance(stu, Student):
                    students.append(stu)

    # 코드가 아닌 키보드로 데이터를 입력 받아야 함
    
    # (1) 입력할 때마다 파일에 저장

    # (2) 입력은 모두 다 받고, 새로 받은 것만 추가하기

    # (3) 기존 + 신규 모두 새로 저장하기
    #       - 기존 성적이 바뀔 경우 



    # students = Student()

    # students = [
    #     Student(12345, "김인하", 100, 98, 80),
    #     Student(12346, "이인하", 100, 10, 100),
    #     Student(12347, "박인하"),
    # ]

    # for stu in students:
    #     print(stu)
    #     print(stu.make_record())
    #     # print(stu.name)
    #     # print(stu.num)
    #     # print(stu.kor, stu.math, stu.eng)
    #     # print(stu.get_average())

    # # print(students[0] == students[1])
    # # print(students[0] != students[1])
    # # print(students[0] < students[1])
    # # print(students[0] > students[1])

    # if not os.path.exists(target_path):
    #     os.mkdir(target_path)

    # # cp949 : 한글 윈도우에서 제공하는 기본 인코딩
    # # utf8 : 다른 언어와 호환을 위한 대표적인 인코딩
    # with open(target_full_file, "a", encoding="utf8") as file:
    #     for stu in students:
    #         file.write(stu.make_record())