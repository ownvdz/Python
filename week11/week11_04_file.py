# 2023-11-09

scores = [
    ["김인하", "2", "컴퓨터정보"],
    ["이인하","1", "컴퓨터정보"],
    ["박인하", "3", "컴퓨터정보"],
]

with open("c:\\test_b\\test_3.txt", "w") as file:
    for score in scores:
        w_data = "|".join(score)
        file.write(w_data + "\n")
    #file.close()

result = []
with open("c:\\test_b\\test_3.txt", "r") as file:
    for line in file:
        line = line.strip()
        datas = line.split("|")
        result.append(datas)
        # print(line)
    #file.close()
print(result)