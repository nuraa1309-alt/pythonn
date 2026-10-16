electricity_usage = float(input("Enter the electricity usage in kWh: "))
if electricity_usage < 0:
    print("Invalid electricity usage. Please enter a non-negative value.")  
elif electricity_usage <= 100:
    rate = 0.08
elif 100 < electricity_usage <= 300:
    rate = 0.12
else:
    rate = 0.15
print("Electricity usage:", electricity_usage, "kWh")
print("Rate per kWh:", rate, "AZN")
print("Total bill:", electricity_usage * rate, "AZN")
