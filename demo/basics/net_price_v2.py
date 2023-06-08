# Take price, calculate discount @12% and display netprice

# input
price = int(input("Enter price :"))

# process
discount = price * 12 // 100
net_price = price - discount

# Output
print(f"Price        {price:8}")
print(f"- Discount   {discount:8}")
print(f"Net price    {net_price:8}")
