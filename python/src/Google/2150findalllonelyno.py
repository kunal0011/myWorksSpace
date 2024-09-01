from collections import Counter


class Solution:
    def findLonely(self, nums: list[int]) -> list[int]:
        count = Counter(nums)
        lonely_numbers = []

        for num in nums:
            if count[num] == 1 and count[num - 1] == 0 and count[num + 1] == 0:
                lonely_numbers.append(num)

        return lonely_numbers
