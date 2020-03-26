students = {'Harry': 37.21, 'Berry': 37.21,
            'Tina': 37.2, 'Akriti': 41, 'Harsh': 39}


print(*sorted(
    [student for student, score in students.items() if score == (sorted(set(students.values()))[1])]), sep="\n")
