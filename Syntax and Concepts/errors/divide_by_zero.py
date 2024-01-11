def divide(a, b):
    try: 
        return print(a/b) 
    except ZeroDivisionError:
        print("you cant divide by zero")
        return None 
    
result = divide(10,0)
if result is not None: 
    print(result)