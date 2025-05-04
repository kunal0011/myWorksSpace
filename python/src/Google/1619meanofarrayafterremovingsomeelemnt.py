"""
LeetCode 1619. Mean of Array After Removing Some Elements

Problem Statement:
Given an integer array arr, return the mean of the remaining integers after removing
the smallest 5% and the largest 5% of the elements. Answers within 10^-5 of the actual answer
will be considered accepted.

Time Complexity: O(nlogn) due to sorting
Space Complexity: O(1) as we modify array in-place
"""

class Solution:
    def trimMean(self, arr: list[int]) -> float:
        # Logic:
        # 1. Sort array to easily identify top and bottom 5%
        # 2. Calculate number of elements to remove from each end (n/20 for 5%)
        # 3. Take subarray excluding removed elements
        # 4. Calculate mean of remaining elements
        
        arr.sort()
        n = len(arr)
        trim = n // 20  # 5% = 1/20
        trimmed_arr = arr[trim: n - trim]
        return sum(trimmed_arr) / len(trimmed_arr)


# Test driver
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3],  # Expected: 2.00000
        [6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0],  # Expected: 4.00000
        [6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4],  # Expected: 4.77778
        [9,7,8,7,7,8,4,4,6,8,8,7,6,8,8,9,2,6,0,2],   # Expected: 7.00000
    ]
    
    for i, arr in enumerate(test_cases):
        result = solution.trimMean(arr)
        print(f"Test case {i + 1}:")
        print(f"Array: {arr}")
        print(f"Mean after removing 5% smallest and largest: {result:.5f}")
        n = len(arr)
        trim = n // 20
        sorted_arr = sorted(arr)
        print(f"Removed elements: {sorted_arr[:trim]} and {sorted_arr[-trim:]}")
        print()
