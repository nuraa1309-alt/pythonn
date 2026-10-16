phone = input()
reqemdirmi = False
for s in phone:
    if s < '0' or s > '9':
        reqemdirmi = True
        break
if phone == "":
    print("Empty input is invalid")
elif len(phone) != 10:
    print("Must be exactly 10 digits")
elif  reqemdirmi:
    print("Digits only")
elif phone[0] != '0':
    print("Must start with 0")
else:
    prefix = phone[:3]
    match prefix:
        case "050" | "051" | "055" | "070" | "077" | "099":
            print("Phone number accepted")
        case _:
            print("Invalid prefix")