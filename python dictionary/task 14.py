'''Task 15: Compute Total from Nested Dictionary
cart = {
    "item1": {"price": 100, "qty": 2},
    "item2": {"price": 50, "qty": 5},
    "item3": {"price": 20, "qty": 10}
}
👉 Compute total bill = sum of price * qty.
Output: 650'''

cart = {
    "item1": {"price": 100, "qty": 2},
    "item2": {"price": 50, "qty": 5},
    "item3": {"price": 20, "qty": 10}
}

total=0
for item in cart:
    price=cart[item]["price"]
    qty=cart[item]["qty"]
    total+=price*qty
print("total bill:",total)