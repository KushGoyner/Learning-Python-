age = int(input("Enter the age of the person:"))


if age>59:
    print("Senior")
elif age > 19:
    print("Adult")
elif age>12 :
    print("Teenage")
else:
    print("Child")