day_number = int(input("Enter the day number (1-7): "))
match day_number:
    case 1:
        print("Monday", "Study day")
    case 2:
        print("Tuesday", "Study day")
    case 3:
        print("Wednesday", "Study day")
    case 4:
        print("Thursday", "Study day")
    case 5:
        print("Friday", "Study day")
    case 6:
        print("Saturday", "Weekend")
    case 7:
        print("Sunday", "Weekend")
    case _:
        print("Invalid day")