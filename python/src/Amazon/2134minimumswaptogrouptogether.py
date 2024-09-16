class Solution:
    def minSwaps(self, nums):
        n = len(nums)
        total_ones = sum(nums)  # Count total number of 1's
        if total_ones == 0:  # No 1's, no swaps needed
            return 0

        # Double the array to handle circular nature
        nums = nums + nums

        # Initial window: count number of 1's in the first window of size total_ones
        current_ones = sum(nums[:total_ones])
        max_ones_in_window = current_ones

        # Sliding window: move through the array and update the window
        for i in range(1, n):
            current_ones += nums[i + total_ones - 1] - nums[i - 1]
            max_ones_in_window = max(max_ones_in_window, current_ones)

        # Minimum swaps needed
        return total_ones - max_ones_in_window


# Test the solution
if __name__ == "__main__":
    sol = Solution()

    # Test case 1: Example from Leetcode
    nums = [1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1]
    print(sol.minSwaps(nums))  # Expected output: 3

    # Test case 2: No 1's in the array
    nums = [0, 0, 0, 0]
    print(sol.minSwaps(nums))  # Expected output: 0

    # Test case 3: All 1's in the array
    nums = [1, 1, 1, 1]
    print(sol.minSwaps(nums))  # Expected output: 0
