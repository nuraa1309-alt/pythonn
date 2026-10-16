stored_pin = "0427"
pin = input()
reqemdirmi = 0
for s in pin:
    if s < '0' or s > '9':
        reqemdirmi = 13
        break
if pin == "":
    print("PIN is required")
elif len(pin) != 4:
    print("PIN must have 4 digits")
elif reqemdirmi == 13:
    print("Digits only")
elif pin == stored_pin:
    print("Access granted")
else:
    print("Incorrect PIN")