from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        # lengths[i] will be the length of the LIS ending at index i
        lengths = [1] * n
        # counts[i] will be the number of LIS ending at index i
        counts = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if lengths[j] + 1 > lengths[i]:
                        lengths[i] = lengths[j] + 1
                        # reset count because we found a longer sequence
                        counts[i] = counts[j]
                    elif lengths[j] + 1 == lengths[i]:
                        # found another sequence of the same length
                        counts[i] += counts[j]

        # Find the length of the longest increasing subsequence
        longest = max(lengths)

        # Sum up the counts of the subsequences that have the longest length
        return sum(count for length, count in zip(lengths, counts) if length == longest)
