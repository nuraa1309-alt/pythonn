travel_distance = float(input("Enter the travel distance in kilometers: "))
if travel_distance < 0: 
    print("Invalid distance. Please enter a non-negative value.")
elif 0 <= travel_distance <= 5:
    rate = 0.70
elif 5 < travel_distance <= 15:
    rate = 0.60
else:
    rate = 0.50
starting_fee = 2
print("starting fee:", starting_fee, "AZN")
print("distance fee:", travel_distance * rate, "AZN")
print("Total fare:", starting_fee + (travel_distance * rate), "AZN")