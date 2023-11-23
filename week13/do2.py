# 2023-11-23
import score as sc

# step1
print("step1", "-" * 10)
score1 = sc.Score1()
print(score1)
print(score1.kor)
print(score1.eng)
print(score1.math)

score1.kor = 100
score1.eng = 40
score1.math = 99

print(score1.kor)
print(score1.eng)
print(score1.math)

# step2
print("step2", "-" * 10)
score2 = sc.Score3(10, 20, 30)
print(score2)
print(score2.scores["kor"])
del score2.scores["kor"]
del score2.scores["eng"]
del score2.scores["math"]
print(score2)
# print(score2.eng)
# print(score2.math)

# step3
print("step3", "-" * 10)
score3 = sc.Score4("kor", "eng", "math")
print(score3.scores)

# step4
print("step4", "-" * 10)
score4 = sc.Score5()
print(score4)

score5 = sc.Score5(kor=10, eng=20)
print(score5)
print(score5.scores)