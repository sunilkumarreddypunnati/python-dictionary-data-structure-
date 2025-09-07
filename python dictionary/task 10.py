'''Task 10: Nested Dictionary Lookup
students = {
    "Alice": {"age": 20, "course": "Math"},
    "Bob": {"age": 22, "course": "Physics"}
}
👉 Print Bob’s course.'''
students = {
    "Alice": {"age": 20, "course": "Math"},
    "Bob": {"age": 22, "course": "Physics"}
}
print(students.get("Bob")["course"])