def avg_score(dic):
    if len(dic.keys()):
        return sum(dic.values())/len(dic.values())

scores={"kim":95, "lee":65}
avg = avg_score(scores)

if avg != None:
    print(f"평균:{avg}")
else:
    print("점수가 없음")