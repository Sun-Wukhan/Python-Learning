file_name  = "conditionals.txt"

def what_day_is_it(): 
    try: 
        text = input("What would you like to write: ")
        text_int = int(text)
    
        with open(file_name, "w") as file: 
            if text_int == 1: 
                file.write("Monday")
            elif text_int == 2:
                file.write("Tuesday")
            elif text_int == 3:
                file.write("Wednesday")
            elif text_int == 4:
                file.write("Thursday")
            elif text_int == 5:
                file.write("Friday")
            elif text_int == 6:
                file.write("Saturday")
            elif text_int == 7:
                file.write("Sunday")
            else:
                file.write("Not a Valid Day Broski")
    except ValueError: 
        print("Please Enter a Valid Number")
        

what_day_is_it()