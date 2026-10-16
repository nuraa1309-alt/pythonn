product_code = input()
qty_str = input()
coupon = input()
delivery_code = input()
qty_digits = True
for s in qty_str:
    if s < '0' or s > '9':
        qty_digits = False
        break
match product_code:
    case 'K':
        product_name = "Keyboard"
        unit_price = 40
    case 'M':
        product_name = "Mouse"
        unit_price = 20
    case 'H':
        product_name = "Headphones"
        unit_price = 60
    case _:
        product_name = ""

if not product_name:
    print("Invalid product code")
elif qty_str == "":
    print("Quantity is required")
elif not qty_digits:
    print("Invalid quantity format")
else:
    qty = int(qty_str)
    if qty < 1 or qty > 5:
        print("Quantity must be between 1 and 5")
    elif coupon != "NONE" and coupon != "SAVE10":
        print("Invalid coupon code")
    else:
        subtotal = unit_price * qty
        
        if coupon == "SAVE10" and subtotal < 100:
            print("Coupon not eligible")
        else:
            match delivery_code:
                case 'P':
                    delivery_fee = 0
                case 'S':
                    discounted_subtotal = subtotal * 0.9 if coupon == "SAVE10" else subtotal
                    delivery_fee = 0 if discounted_subtotal >= 80 else 5
                case _:
                    delivery_fee = -1 
            if delivery_fee == -1:
                print("Invalid delivery code")
            else:
                discount = subtotal * 0.1 if coupon == "SAVE10" else 0
                final_total = (subtotal - discount) + delivery_fee
                
                print(product_name)
                print(qty)
                print(subtotal)
                print(discount)
                print(delivery_fee)
                print(final_total)