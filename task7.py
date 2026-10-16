userage = int(input("Please enter your age: "))
if 0 <= userage <=12:
    print("You are a child.")
elif 13 <= userage <= 17:
    print("You are a teenager.")
elif 18 <= userage <= 64:
    print("You are an adult.")  
elif userage >= 65:
    print("You are a senior .")
else:
    print("Invalid age entered.")