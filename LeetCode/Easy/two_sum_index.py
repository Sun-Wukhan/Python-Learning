def two_sum_step(nums, target):
    nums_map = {}
    for i, num in enumerate(nums):
        difference = target - num
        print(f"DIFF: {difference}")
        print(f"NUMBER: {num}")
        if difference in nums_map:
            # If the difference is already in the map, return the pair of indices.
            return [nums_map[difference], i]
        # Store the current number and its index in the map.
        nums_map[num] = i
        print(nums_map)
        # Print the current state of the nums_map for visualization.
        print("Step", i, ":", nums_map)
    # If no pair is found, return None.
    return None

print(two_sum_step([2, 7, 11, 15], 26))