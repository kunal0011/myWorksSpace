class Solution:
    def minOperations(self, nums, x):
        target = sum(nums) - x
        if target == 0:
            return len(nums)  # The entire array sums to x

        n = len(nums)
        max_len = -1
        current_sum = 0
        left = 0

        for right in range(n):
            current_sum += nums[right]

            # Shrink the window if the sum exceeds the target
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1

            # Check if we found a subarray that sums to target
            if current_sum == target:
                max_len = max(max_len, right - left + 1)

        return len(nums) - max_len if max_len != -1 else -1


# Testing
solution = Solution()
nums = [1, 1, 4, 2, 3]
x = 5
print("Python Test Result:", solution.minOperations(
    nums, x))  # Output should be 2
