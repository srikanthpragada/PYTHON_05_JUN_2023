# Take salary and calculate net salary by adding HRA and DA

salary = int(input("Enter salary :"))

if salary > 50000:
    hra = salary * 20 / 100
    da = salary * 10 / 100
else:
    hra = salary * 15 / 100
    da = salary * 8 / 100

net_salary = salary + hra + da
print(f"Net salary  {net_salary:8.0f}")
