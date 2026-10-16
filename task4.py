score = int(input("Enter the score: "))
if  score <0 :
    print("Invalid score. ")
elif score > 100:
    print("Invalid score. ")
else:
    if score >= 91:
        print("Grade: A")
    elif score >= 81:
        print("Grade: B")
    elif score >= 71:
        print("Grade: C")
    elif score >= 61:
        print("Grade: D")
    elif score >= 51:
        print("Grade: e")
    else :
        print("Grade: F")

