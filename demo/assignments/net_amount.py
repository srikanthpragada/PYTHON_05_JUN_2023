# Program to print net amount after giving discount based on qty

price = int(input('Enter the price:'))
quantity = int(input('Enter the quantity:'))

amount = price * quantity
if quantity > 2:
    discount_rate = 20
else:
    discount_rate = 10

discount = amount * discount_rate / 100
net_amount = amount - discount

print(f"Amount              {amount:8.0f}")
print(f"- Discount of {discount_rate}%  {discount:8.0f}")
print(f"Net Amount          {net_amount:8.0f}")
