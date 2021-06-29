"""
There are  students in this class whose names and grades are assembled to build the following list:

python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

The lowest grade of  belongs to Tina. The second lowest grade of  belongs to both Harry and Berry, so we order their
names alphabetically and print each name on a new line.
"""

if __name__ == "__main__":
    students_grade = []
    for _ in range(int(input())):
        # take a name and score as input
        name = input()
        score = float(input())
        # store name and score in nested list "student_grade"
        students_grade.append([name, score])
        # Make a Unique_sorted_score_list that is unique(using set())
        # and sorted(using sorted()) scores
    sorted_score = sorted(list(set([x[1] for x in students_grade])))
    second_lowest = sorted_score[1]
    low_final_list = []
    for student in students_grade:
        if second_lowest == student[1]:
            low_final_list.append(student[0])
    for student in sorted(low_final_list):
        print(student)