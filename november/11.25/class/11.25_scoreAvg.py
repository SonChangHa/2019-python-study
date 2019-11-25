students = int(input("enter the number of students>> "))

scores = []
scoreSum = 0

for i in range(students):
    value = int(input("enter the score>> "))
    scores.append(value)
    scoreSum += value

scoreAvg = scoreSum / len(scores)

highScoreStudent = 0
for i in range(students):
    if scores[i] >= 80:
        highScoreStudent += 1

print("the average score is ", scoreAvg)
print(highScoreStudent, "students scored 80 or higher")