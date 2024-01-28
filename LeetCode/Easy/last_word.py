

def length_last_word(s): 
    s = s.rstrip()
    
    length = 0 
    
    for char in reversed(s):
        if char == ' ':
            break 
        length += 1
    return length 

print(length_last_word("Hello World"))
