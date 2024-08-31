class Solution:
    def pivotIndex(self, nums):
        total_sum = sum(nums)
        prefix_sum = 0

        for i, num in enumerate(nums):
            # Calculate right sum by subtracting the prefix sum and current element from total sum
            right_sum = total_sum - prefix_sum - num
            if prefix_sum == right_sum:
                return i
            prefix_sum += num

        return -1
