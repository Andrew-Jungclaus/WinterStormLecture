Student_and_scores = {"mary":87,"Andrew":90,"Bill":70,"Leah":80,"Eric":89}
Student_and_scores["sam"]= 78
Student_and_scores["Marrie"]=92
Student_and_scores["Ria"] = 88

print(len(Student_and_scores))

total_Scores = sum(Student_and_scores.values())
a = total_Scores / len(Student_and_scores)

print("The average of the total scores is:", a)

print("Students with scores above the average:")
for student, score in Student_and_scores.items():
    if score > a:
        print(student)



Student_and_score = list(Student_and_scores.values()) # the list() makes a new list within the syntax
Student_and_score.sort()
print(Student_and_score[-1]) 

Student_and_scores.update({"sam":95})
print(Student_and_scores)


