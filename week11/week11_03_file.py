# 2023-11-09
import os

target = "c:\\test_bb\\test01.txt"
if os.path.exists(target):
    file = open(target, 'r')

    data = file.read()
    print(data)



    # lines = file.readlines()
    # print(lines)
    # 
    # for line in lines:
    #     print(line.strip())
    
    
    
    # while True:
    #     line = file.readline()
    #     if not line:
    #         break
    #     if line.strip() == "1학년":
    #         break
    #     print(line.strip())
    
    file.close()