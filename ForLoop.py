student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))
total_score = 0
# Program to find the Total Score
max_score = 0

for score in student_scores:
    total_score += score
print(total_score)

#Program to find the Max score

for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)


#Built in functions to get sum and max scores

print(sum(student_scores))
print(max(student_scores))
