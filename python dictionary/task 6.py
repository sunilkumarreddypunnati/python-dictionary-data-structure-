'''Task 6: Count Frequency of Words
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
👉 Create a dictionary with word counts.
Output: {'apple': 3, 'banana': 2, 'orange': 1}'''

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
count={ }
for word in words:
    if word in count:
        count[word]+=1
    else:
        count[word]=1
print(count)