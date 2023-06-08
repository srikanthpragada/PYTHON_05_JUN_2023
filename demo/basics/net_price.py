# Take price, calculate discount @12% and display netprice

price = int(input("Enter price :"))
discount = price * 12 // 100
net_price = price - discount
print('Net price =', net_price)
