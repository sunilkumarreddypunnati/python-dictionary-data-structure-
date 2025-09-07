'''Task 7: Merge Dictionaries with Addition
sales1 = {"apple": 50, "banana": 30}
sales2 = {"apple": 20, "orange": 10}
👉 Merge them, summing values for common keys.
Output: {'apple': 70, 'banana': 30, 'orange': 10}'''

sales1 = {"apple": 50, "banana": 30}
sales2 = {"apple": 20, "orange": 10}
merged_sales={}
for key,value in sales1.items():
    merged_sales[key]=value
for key,value in sales2.items():
    if key in merged_sales:
        merged_sales[key]+=value
    else:
        merged_sales[key]=value 
    
print(merged_sales)