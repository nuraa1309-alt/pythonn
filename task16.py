score = int(input("Enter the score: "))
if  score <0  and score > 100:
    print("Invalid score. ")    
else:
    result = "pass" if score >= 51 else "fail"
    print (result)