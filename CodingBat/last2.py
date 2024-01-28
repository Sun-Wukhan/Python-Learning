def last2(str):
  
  if len(str) < 2: 
    return 0 
  
  last2 = str[-2:]
  print("This is the last two:" + last2)
  count = 0 
  
  for i in range(len(str)-2): 
    print(f"i: i+2: {str[i:i+2]}")
    sub = str[i:i+2]
    print(f"This is the:" + sub)

    if sub == last2: 
      count = count + 1
      
  return count

print(last2('hixxhi'))
