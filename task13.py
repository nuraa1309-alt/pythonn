age = int(input("Enter the age: ")) 
monthly_salary = float(input("Enter the monthly salary: "))
loan= float(input("Enter the requested loan amount: "))
if age <=0 or monthly_salary <=0 or loan <=0:
    print(" Please enter a positive value.")
elif age <18:
    print("Loan denied. Applicant is not of legal age.")
else:
    if monthly_salary >= 500:
        if loan <= 10 * monthly_salary:
            print("Loan approved.")
        else:
            print("Loan denied. The requested loan amount exceeds the limit.")
    else:
        print("Loan denied. Monthly salary is below the required threshold.")