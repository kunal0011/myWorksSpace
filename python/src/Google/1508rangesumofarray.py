class Solution:
    def rangeSum(self, nums: list[int], n: int, left: int, right: int) -> int:
        subarray_sums = []
        for i in range(len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]
                subarray_sums.append(current_sum)

        subarray_sums.sort()
        return sum(subarray_sums[left-1:right]) % (10**9 + 7)
