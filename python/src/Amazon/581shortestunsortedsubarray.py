class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        n = len(nums)

        # Step 1: Find the first element from the left that is out of order
        left = 0
        while left < n - 1 and nums[left] <= nums[left + 1]:
            left += 1

        # If the array is already sorted, return 0
        if left == n - 1:
            return 0

        # Step 2: Find the first element from the right that is out of order
        right = n - 1
        while right > 0 and nums[right] >= nums[right - 1]:
            right -= 1

        # Step 3: Find the minimum and maximum within the subarray
        subarray_min = min(nums[left:right+1])
        subarray_max = max(nums[left:right+1])

        # Step 4: Expand the left boundary
        while left > 0 and nums[left - 1] > subarray_min:
            left -= 1

        # Step 5: Expand the right boundary
        while right < n - 1 and nums[right + 1] < subarray_max:
            right += 1

        # Return the length of the subarray
        return right - left + 1


# Test the Solution
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    nums = [2, 6, 4, 8, 10, 9, 15]
    # Output: 5
    print(
        f"Length of the shortest unsorted subarray: {solution.findUnsortedSubarray(nums)}")

    # Test case 2
    nums = [1, 2, 3, 4]
    # Output: 0
    print(
        f"Length of the shortest unsorted subarray: {solution.findUnsortedSubarray(nums)}")

    # Test case 3
    nums = [1, 3, 2, 2, 2]
    # Output: 4
    print(
        f"Length of the shortest unsorted subarray: {solution.findUnsortedSubarray(nums)}")
