

def missing_char(str, n):
    
    front = str[:n]
    print(f"Front: {front}")
    back = str[n+1:]
    print(f"Back: {back}")
    
    return front + back

print(missing_char('kitten', 2))