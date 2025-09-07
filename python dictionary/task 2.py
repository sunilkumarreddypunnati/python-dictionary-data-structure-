'''Task 2: Add a New Key
student = {"name": "Sunil", "age": 25}
👉 Add "city": "Hyderabad" to the dictionary.'''

student = {"name": "Sunil", "age": 25}
student.update({"city":"hyderabad"})
print(student)