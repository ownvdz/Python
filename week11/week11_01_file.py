# 2023-11-09

# try, except <== 예외처리
try:
    # 열고
    # f = open("c:\\test_b\\test01.txt", 'w')
    f = open("c:\\test_e\\test01.txt", 'a')

    # 작업하고
    f.write("김인하\n")
    f.write("컴퓨터정보과\n")
    f.write("1학년\n")
    f.write("이인하|컴퓨터시스템과|2학년\n")
    # print(f)

    # 닫고
    f.close()

except:
    print("폴더가 없나?")

