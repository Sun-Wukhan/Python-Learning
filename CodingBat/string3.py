

def string_splosion(str):
  
  result = ""
  
  for i in range(len(str)): 
     print(f'This is SPARTA: {str[:i+1]}')
     result = result + str[:i+1]

  return result
    

print(string_splosion('Code'))
