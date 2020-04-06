def gradingStudents(grades):
    # Write your code here
    finalGrade = []
    for grade in grades:
        if grade >= 38:
            m5 = ((grade//5)+1)*5
            defgrade = m5 - grade
            if defgrade < 3:
                finalGrade.append(m5)
            else:
                finalGrade.append(grade)
        else:
            finalGrade.append(grade)
    return finalGrade


grades = [73, 67, 38, 33]
print(*gradingStudents(grades), sep="\n")
