

def is_anagram(p1, p2): 
    
    p1 = p1.replace(" ", "").lower()
    p2 = p2.replace(" ", "").lower()
    
    if sorted(p1) == sorted(p2): 
        return print("These are Anagrams")
    else: 
        return print("these are not anagrams")
    

is_anagram("NA V I     D      ", "Di t  aN")