age = int(input("Enter Your Age:"))
day=input("Enter day:")

price = 12 if age>=18 else 8

if day=="wednesday":
    price -= 2

print(price)
