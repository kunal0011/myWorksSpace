from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        total_sum = sum(nums)
        nums.sort(reverse=True)
        subseq_sum = 0

        result = []
        for num in nums:
            subseq_sum += num
            result.append(num)
            if subseq_sum > total_sum - subseq_sum:
                break

        return result


# Testing
solution = Solution()
nums = [4, 3, 10, 9, 8]
# Output should be [10, 9]
print("Python Test Result:", solution.minSubsequence(nums))
