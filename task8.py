purchase = float(input("Enter the purchase amount in AZN: "))
if purchase < 0:
    print("Invalid purchase amount. Please enter a non-negative value.")  
elif purchase < 100:
    d = 0
elif 100 <= purchase < 300:
    d = 10
elif 300 <= purchase < 500:
    d = 15
else:
    d = 20
print ("original price  = ", purchase, "AZN")
print ("discount  = ", d, "%")
print ("final price  = ", purchase - (purchase * d / 100), "AZN")
