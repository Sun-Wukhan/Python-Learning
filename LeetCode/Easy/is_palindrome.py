

def is_palindrome(p1, p2): 
    
    p1.replace(" ", "").lower()
    p2.replace(" ", "").lower()
    
    if p1 == p2[::-1]:
        return print("PALINDROME")
    else: 
        return print("NOT PALINDROME")
    

is_palindrome("NAVID", "DIV5N")