a = int(input("Enter a number: ") )
b = int(input("Enter another number: "))
c = int(input("Enter a third number: "))
if a > b and a > c:
    if b > c:
        print( c, b, a)
    else:
        print( b, c, a)
elif b > a and b > c:
    if a > c:
        print( c, a, b)
    else:
        print( a, c, b) 
else :
    if a > b:
        print( b, a, c)
    else:
        print( a, b, c)
        
           
        
        