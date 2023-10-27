def get_students(dic):
    arr = []
    if len(dic.keys()):
        keys = list(dic.keys())
        for i in range(len(dic.keys())):
            arr.append(keys[i])
        return arr
    
scores={"kim":95, "lee":65}
students = get_students(scores)

if students:
    students=",".join(students)
    print(f"명단:{students}")
else:
    print("학생이 없음")