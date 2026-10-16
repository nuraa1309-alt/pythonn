total = float(input("Enter the order amount (AZN): "))
membership = input("Do you have membership? (yes/no): ")
if total < 0:
    print("Error: Amount cannot be negative")
elif membership != "yes" and membership != "no":
    print("Error: Membership answer must be 'yes' or 'no'")
else:
    fee = 0 if total >= 50 or membership == "yes" else 5
    final_amount = total + fee
print("fee:", fee)
print("final amount:", final_amount)