class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        # Helper function to calculate maximum subarray sum (Kadane's Algorithm)
        def kadane_max(arr):
            max_ending_here = max_so_far = arr[0]
            for num in arr[1:]:
                max_ending_here = max(num, max_ending_here + num)
                max_so_far = max(max_so_far, max_ending_here)
            return max_so_far

        # Helper function to calculate minimum subarray sum (Kadane's Algorithm for min)
        def kadane_min(arr):
            min_ending_here = min_so_far = arr[0]
            for num in arr[1:]:
                min_ending_here = min(num, min_ending_here + num)
                min_so_far = min(min_so_far, min_ending_here)
            return min_so_far

        # Step 1: Find non-circular max subarray sum
        max_subarray_sum = kadane_max(nums)

        # Step 2: Find circular max subarray sum
        total_sum = sum(nums)
        min_subarray_sum = kadane_min(nums)
        circular_max_sum = total_sum - min_subarray_sum

        # Step 3: Handle case where all numbers are negative
        if max_subarray_sum < 0:
            return max_subarray_sum

        # Step 4: Return the maximum of non-circular and circular subarray sum
        return max(max_subarray_sum, circular_max_sum)


# Test cases
def test_max_subarray_sum_circular():
    sol = Solution()

    # Test case 1: Normal array with no circular sum needed
    assert sol.maxSubarraySumCircular([1, -2, 3, -2]) == 3

    # Test case 2: Circular array max
    assert sol.maxSubarraySumCircular([5, -3, 5]) == 10

    # Test case 3: All negative values
    assert sol.maxSubarraySumCircular(
        [-3, -2, -3]) == -2  # Max of a single element

    # Test case 4: Circular sum across array
    assert sol.maxSubarraySumCircular([3, -1, 2, -1]) == 4

    # Test case 5: Larger array with wrap-around maximum
    assert sol.maxSubarraySumCircular([3, -2, 2, -3]) == 3

    print("All test cases passed!")


# Run the tests
test_max_subarray_sum_circular()
