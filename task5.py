a = float(input("Enter a number: "))
b = float(input("Enter another number: "))
c = float(input("Enter a third number: "))
if a > b and a > c:
    print("The largest number is:", a)
elif b > a and b > c:
    print("The largest number is:", b)
elif c > a and c > b:
    print("The largest number is:", c)
else:
    print("There is a tie for the largest number.")