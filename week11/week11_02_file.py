# 2023-11-09
import os

if not os.path.exists("c:\\test_bb"):
    os.mkdir("c:\\test_bb")

file = open("c:\\test_bb\\test02.txt", 'w')

scores = {'math' : 90, 'kor' : 100, 'eng' : 40}
for k, v in scores.items() :
    data = f"{k}, {v}\n"
    file.write(data)


file.close()

