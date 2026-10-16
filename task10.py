m = float(input("Enter the amount of money: "))
balance = 1000
if m <= 0:  
    print("Invalid amount. ") 
else:
    if m > balance:
        print("Insufficient balance.")
    else:
        remaining_balance = balance - m
        print("Remaining balance:", remaining_balance)