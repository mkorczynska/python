age = int(input("Enter your age: "))
age = int(age)

if age > 17:
    print("can see a rated R movie")
elif 17 > age > 12:
    print("can see a rated PG-13 movie")
else:
    print("can only see rated PG movies")

num = int(input("give me a number to check: "))
check = int(input("give me a number to divide by: "))

if num % 4 == 0:
    print(num, "is a multiple of 4")
elif num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")

if num % check == 0:
    print(num, "divides evenly by", check)
else:
    print(num, "does not divide evenly by", check)