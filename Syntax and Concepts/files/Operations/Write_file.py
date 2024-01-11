file_name = "output.txt"

with open(file_name, "a") as file: 
    user_input = input("Enter something you would like to write to the file: ")
    file.write(user_input + "\n" )