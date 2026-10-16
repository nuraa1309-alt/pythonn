student_id = input()
if student_id == "":
    print("Empty input is invalid")
elif len(student_id) != 8:
    print("Must be exactly 8 digits")
else:
    sehv_var = 1
    for simvol in student_id:
        if simvol < '0' or simvol > '9':
            sehv_var = 3
            break
            
    if sehv_var == 3:
        print("Only digits are allowed")
    else:
        print("Student ID accepted")