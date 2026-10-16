code = input()
quantity = int(input())
if 1 <= quantity <= 10:
    match code:
        case 'T':
            drink = "Tea"
            price = 2
        case 'C':
            drink = "Coffee"
            price = 4
        case 'J':
            drink = "Juice"
            price = 3
        case _:
            drink = ""        
    if drink:
        total = quantity * price
        order_type = "Large order" if total >= 20 else "Regular order"
        print(drink)
        print(quantity)
        print(total)
        print(order_type)
    else:
        print("Invalid code")
else:
    print("Invalid quantity")