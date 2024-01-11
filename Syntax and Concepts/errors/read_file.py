def read_and_write_file(file_name):
    try:
        f = open(file_name, "r")
        number = int(f.readline())
    except FileNotFoundError: 
        print("File Not Found")
        return None
    except ValueError: 
        print("No Value")
        return none 
    else: 
        print("Number read successfully", number)
        process_number = number * 2
        return print(process_number)
    finally: 
        print("Closing this method")
        f.close()

read_and_write_file("test.txt")