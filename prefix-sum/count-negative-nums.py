def count_negatives_in_range(arr, queries):
    # Step 1: Build prefix count array for negative numbers
    n = len(arr)
    prefix_count = [0] * n
    prefix_count[0] = 1 if arr[0] < 0 else 0
    
    for i in range(1, n):
        prefix_count[i] = prefix_count[i - 1] + (1 if arr[i] < 0 else 0)
    
    # Step 2: Answer queries using prefix count array
    results = []
    for l, r in queries:
        if l == 0:
            results.append(prefix_count[r])
        else:
            results.append(prefix_count[r] - prefix_count[l - 1])
    
    return results

# Example input
arr = [1, -2, 3, -4, 5, -6]
queries = [(1, 4), (0, 5), (2, 3)]

print(count_negatives_in_range(arr, queries))