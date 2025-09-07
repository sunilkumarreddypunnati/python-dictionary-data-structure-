'''Task 12: Character Count
text = "hello world"
👉 Count frequency of each character (ignore spaces).
Output: {'h':1, 'e':1, 'l':3, 'o':2, 'w':1, 'r':1, 'd':1}'''

text = "hello world"
count={}
for char in text:
    if char in count:
        count[char]+=1
    else:
        count[char]=1
print(count)
