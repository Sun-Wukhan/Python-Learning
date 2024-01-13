def two_sum_numbers(nums, target):
    nums_map = {}
    for num in nums:
        difference = target - num
        if difference in nums_map:
            # If the difference is already in the map, return the pair of numbers.
            print(f"DIFFERENCE: {difference}")
            print(f"NUMBER: {num}")
            return [difference, num]
        # Store the current number in the map.
        nums_map[num] = True
        # Print the current state of the nums_map for visualization.
        print("Current state of nums_map:", nums_map)
    # If no pair is found, return None.
    return None

# Running the function with the specified input
print(two_sum_numbers([2, 7, 11, 15], 26))



