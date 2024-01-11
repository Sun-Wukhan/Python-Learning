file_name = "trial.txt"

def try_reading_file():
    try: 
        with open(file_name, "a") as file: 
            user_input = input("Enter what you would like to add: ") 
            user_input_int = int(user_input)
            file.write(str(user_input_int))       
    except FileNotFoundError: 
        print("File not found")
        return None
    except ValueError: 
        print("File has No Value that is a number")
        return None 
    else: 
        print("This is the else block and it shows this was a success")
    finally: 
        print("Mission Success")
        file.close()
        
try_reading_file()