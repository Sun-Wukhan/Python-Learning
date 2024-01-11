file_name = "status.txt"

def facebook_status(): 
    
    status = input("Write a facebook status: ")
    
    try: 
        with open(file_name, "a") as file: 
            file.write(status)
    except FileNotFoundError: 
        print("File Not Found")
        
facebook_status()