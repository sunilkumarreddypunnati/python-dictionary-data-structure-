'''Task 14: Sort Dictionary by Value
scores = {"Alice": 85, "Bob": 72, "Charlie": 90, "David": 60}
👉 Sort dictionary by values (descending).
Output: [('Charlie', 90), ('Alice', 85), ('Bob', 72), ('David', 60)]'''

scores = {"Alice": 85, "Bob": 72, "Charlie": 90, "David": 60}
sorted_scores=sorted( scores.items(),key=lambda item :item[1], reverse =True)
print(sorted_scores)