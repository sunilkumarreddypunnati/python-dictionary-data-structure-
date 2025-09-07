'''Task 11: Group by Value
grades = {"Alice": "A", "Bob": "B", "Charlie": "A", "David": "C"}
👉 Group students by grade.
Output: {'A': ['Alice', 'Charlie'], 'B': ['Bob'], 'C': ['David']}'''

grades = {"Alice": "A", "Bob": "B", "Charlie": "A", "David": "C"}

group={}

for student, grade in grades.items():
    if grade not in group:
        group[grade]=[]
    group[grade].append(student)
print(group)