exam_score = int(input("Enter the exam score: "))
school_score = int(input("Enter the school score: "))
age = int(input("Enter the age: "))
if exam_score < 0 or school_score < 0 or age < 0:
    print("Invalid input. Scores and age must be non-negative.")
if 0 <= exam_score <= 700 and 0 <= school_score <= 100:    
  if age <16:
    print("Application rejected due to age.")
  elif 600 <= exam_score <= 700 :
    print("scholarship granted")
  elif 450 <= exam_score <= 599:
    print(" Application accepted ")
  elif 300 <= exam_score <= 449 and school_score >= 80:
    print("Application accepted")   
  else:
    print("Application rejected due to low scores.")
else:
    print("Invalid input. Exam score must be between 0 and 700, and school score must be between 0 and 100.")