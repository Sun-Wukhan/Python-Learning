


def longest_length(s):
    
    words = s.split() 
    longest_word = ""
    max_length = 0
    
    for word in words: 
        word = word.strip(".,!?")
        
        if len(word) > max_length: 
            max_length = len(word)
            longest_word = word
    
    return longest_word

input_string = "This is a sample sentence with some longer words like elephant and hippopotamus."
result = longest_length(input_string)
print("The longest word in the string is:", result)