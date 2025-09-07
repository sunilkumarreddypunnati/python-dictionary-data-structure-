'''Task 5: Loop Through Dictionary
student = {"name": "Sunil", "age": 26, "course": "Python"}
👉 Print in format:
name -> Sunil
age -> 26
course -> Python'''

student = {"name": "Sunil", "age": 26, "course": "Python"}
for key,value in student.items():
    print(key ,"->", value )