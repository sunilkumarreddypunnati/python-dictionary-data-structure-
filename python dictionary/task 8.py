'''Task 8: Filter Dictionary
marks = {"Alice": 85, "Bob": 65, "Charlie": 90, "David": 55}
👉 Create a new dictionary with only students scoring above 70.
Output: {'Alice': 85, 'Charlie': 90}'''

marks = {"Alice": 85, "Bob": 65, "Charlie": 90, "David": 55}
new={}
for key,value in marks.items():
    if value>75 :
        new[key]=value
print(new)

    