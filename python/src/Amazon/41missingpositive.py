class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)

        # Step 1: Place each number in its correct position if possible
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] and nums[nums[i] - 1]
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        # Step 2: Identify the first index that does not have the correct value
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # If all positions are correct, the missing number is n + 1
        return n + 1
