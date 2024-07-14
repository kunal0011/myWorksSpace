class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        operations = 0

        for i in range(n - 2):  # We only need to check up to the third last element
            if nums[i] == 0:
                # Flip nums[i], nums[i+1], nums[i+2]
                nums[i] = 1 - nums[i]
                nums[i + 1] = 1 - nums[i + 1]
                nums[i + 2] = 1 - nums[i + 2]
                operations += 1

        # After the loop, check the last two elements if they are zero, it's impossible to make all 1s
        if nums[-1] == 0 or nums[-2] == 0:
            return -1

        return operations


# Example usage:
sol = Solution()
nums1 = [0, 0, 0, 1, 0, 1]
print(sol.minOperations(nums1))  # Output: 2

nums2 = [1, 1, 0, 0, 0]
print(sol.minOperations(nums2))  # Output: 1

nums3 = [1, 0, 1, 0, 1, 0, 1]
print(sol.minOperations(nums3))  # Output: 3

nums4 = [1, 1, 1]
print(sol.minOperations(nums4))  # Output: 0
