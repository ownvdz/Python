# 2023-11-23
import score as sc

scores = []
scores.append(sc.Score(kor=20, eng=30, math=40))
scores.append(sc.Score(kor=20, eng=30))
scores.append(sc.Score(kor=20, math=40))
scores.append(sc.Score())

for score in scores:
    print(score.get_average())
    # print(sc.Score.get_average(score))
    # avg = sum(score.scores.values()) / len(score.scores)
    # print(avg)

print(scores[0].add_subject("kor", 10))
print(scores[0].add_subject("sci", 10))