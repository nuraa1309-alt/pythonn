balance = 1000
stored_pin = "0427"
pin = input()
amount_str = input()
pin_digits = True
for s in pin:
    if s < '0' or s > '9':
        pin_digits = False
        break
amount_digits = True
for s in amount_str:
    if s < '0' or s > '9':
        amount_digits = False
        break
if pin == "":
    print("PIN is required")
elif len(pin) != 4 or not pin_digits:
    print("Invalid PIN format")
elif pin != stored_pin:
    print("Incorrect PIN")
elif amount_str == "":
    print("Amount is required")
elif not amount_digits:
    print("Invalid amount format")
else:
    amount = int(amount_str)
    if amount < 10 or amount > 500:
        print("Amount must be between 10 and 500")
    elif amount % 10 != 0:
        print("Amount must be a multiple of 10")
    else:
        fee = 0 if amount <= 200 else 2
        
        if amount + fee > balance:
            print("Insufficient balance")
        else:
            new_balance = balance - (amount + fee)
            print(amount)
            print(fee)
            print(new_balance)