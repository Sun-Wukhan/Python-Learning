

def two_sum(nums, target): 
    nums_map = {}
    
    for i, num in enumerate(nums): 
        difference = target - num 
        
        if difference in nums_map: 
            return [nums_map[difference], i]
        
       
        nums_map[num] = i
    
    return None

print(two_sum([2, 7, 11, 15], 26))