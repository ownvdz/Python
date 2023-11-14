f = open("c:\\202344053\\list.txt", "w")

while True : 
    Name = input("이름을 넣어주세요.(종료시:바로엔터) : ")

    if Name :
        korScore = input("국어 점수 :")
        engScore = input("영어 점수 :")
        mathScore = input("수학 점수 :")

        f.write(Name)
        f.write(","+korScore)
        f.write(","+engScore)
        f.write(","+mathScore+"\n")
    else :
        break