'''
What is Prefix Sum?
-The Prefix Sum is an array technique that allows you to efficiently calculate the sum of elements in a subarray or range of elements within an array. The idea is to preprocess an array to store cumulative sums at each index, making range sum queries faster.

-In simpler terms, prefix sum stores the sum of all the elements in the array up to a particular index. Once the prefix sum array is computed, you can find the sum of elements between any two indices in constant time.

How Prefix Sum Works:
Given an array arr of size n, the prefix sum array (prefixSum) is constructed such that:
    prefixSum[i] = arr[0] + arr[1] + ... + arr[i] for all 0 <= i < n.
Thus, prefixSum[i] stores the sum of all elements from arr[0] to arr[i].

-sum(arr[l...r]) = prefixSum[r] - prefixSum[l-1]

Applications and Use Cases:
-Range Sum Queries: Prefix sums are commonly used when you need to repeatedly compute the sum of elements in a subarray. Instead of recalculating the sum each time (which would take O(n) time), you can use a prefix sum array to answer each query in constant time.

Problem Example: Given an array of integers, answer multiple queries asking for the sum of elements between any two indices.
-Subarray Problems: Prefix sums can be extended to calculate other properties like the maximum subarray sum or counting the number of negative numbers in a range.

-Frequency Count Problems: Prefix sums can be applied when you need to find the frequency of certain events in a range of elements, such as in counting prefix occurrences.

-Efficient Computation of Range Queries: If you have a problem where you need to calculate certain properties over different subarrays multiple times (like sum, min, max, or count), prefix sums provide a great way to preprocess the data and answer queries quickly.
'''

def range_sum(arr, queries):
    # Step 1: Compute prefix sum array
    n = len(arr)
    prefixSum = [0] * n
    prefixSum[0] = arr[0]
    for i in range(1, n):
        prefixSum[i] = prefixSum[i-1] + arr[i]
    
    # Step 2: Answer each query
    results = []
    for l, r in queries:
        if l == 0:
            results.append(prefixSum[r])
        else:
            results.append(prefixSum[r] - prefixSum[l-1])
    
    return results

# Example input
arr = [2, 4, 6, 8, 10]
queries = [(1, 3), (0, 2), (2, 4)]

print(range_sum(arr, queries))