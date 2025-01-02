def subarray_with_sum(arr, target):
    prefix_sum = set()
    current_sum = 0
    
    for num in arr:
        current_sum += num
        if current_sum == target:
            return True
        if (current_sum - target) in prefix_sum:
            return True
        prefix_sum.add(current_sum)
    
    return False

# Example input
arr = [1, 2, 3, 7, 5]
target = 12

print(subarray_with_sum(arr, target))  # Output: True (subarray [2, 3, 7] sums to 12)