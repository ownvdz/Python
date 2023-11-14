import os
path_name = "c:/본인학번"
full_filename = path_name + "/list.txt"
if not os.path.isdir(path_name):
    os.mkdir(full_filename)
f = open(full_filename, "a")
while True:
    Name = input("이름을 넣어주세요.(종료시:바로엔터) : ")
    if not Name :
        break
    korScore = input("국어 점수 :")
    engScore = input("영어 점수 :")
    mathScore = input("수학 점수 :")

    f.write(Name)
    f.write(","+korScore)
    f.write(","+engScore)
    f.write(","+mathScore+"\n")
f.close()
