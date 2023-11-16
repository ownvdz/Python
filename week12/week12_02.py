# 2023-11-16        # p.366

list_score = [10, 20, 30, 40, 50, 60]
try: # 실행하고자 하는 코드
    number1 = input("분자:")
    number1 = int(number1)

    number2 = input("분모:")
    number2 = int(number2)

    result = number1 // number2
    print(result)

    print(list_score[result])
except:
    print("예외가 발생")
    print("비정상 종료")