from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))

    # Custom comparator for sorting
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0

        # Sort nums using the custom comparator
        nums.sort(key=cmp_to_key(compare))

        # Join sorted numbers to form the largest number
        largest_num = ''.join(nums)

        # Handle case where the result is "000...0"
        if largest_num[0] == '0':
            return '0'

        return largest_num
