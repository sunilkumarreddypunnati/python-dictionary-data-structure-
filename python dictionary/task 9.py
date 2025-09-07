'''Task 9: Invert Dictionary
students = {"Alice": 101, "Bob": 102, "Charlie": 103}
👉 Make values keys and keys values.
Output: {101: "Alice", 102: "Bob", 103: "Charlie"}'''

students = {"Alice": 101, "Bob": 102, "Charlie": 103}
inverted={}
for key,value in students.items():
    inverted[value]=key
print(inverted)
    