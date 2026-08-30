a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
if a > b:
    print("The first number is greater than the second number.", a, ">", b)
elif a < b:
    print("The first number is less than the second number.", a, "<", b)
else:
    print("Both numbers are equal.", a, "=", b)
    