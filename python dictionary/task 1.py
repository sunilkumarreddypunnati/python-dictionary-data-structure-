'''Task 1: Access a Value
student = {"name": "Sunil", "age": 25, "course": "Python"}
👉 Print the value of "course"'''

student = {"name": "Sunil", "age": 25, "course": "Python"}
print(student["course"])#Direct access. 
print(student.get("course"))#Safe access