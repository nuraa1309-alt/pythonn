a = int(input("Enter a value for a: "))
b = int(input("Enter a value for b: "))
c = int(input("Enter a value for c: "))
if a + b > c:
    if a + c > b:
        if b + c > a:
            if a==b==c:
                print("The triangle is equilateral.")
            elif a==b or b==c or a==c:
                print("The triangle is isosceles.")
            else:
                print("The triangle is scalene.")   
        else:
            print("The triangle is not valid.")
    else:               
        print("The triangle is not valid.")
else:
    print("The triangle is not valid.")
                