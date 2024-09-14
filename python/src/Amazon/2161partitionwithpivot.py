from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_than_pivot = []
        equal_to_pivot = []
        greater_than_pivot = []

        # Partition the array into three categories
        for num in nums:
            if num < pivot:
                less_than_pivot.append(num)
            elif num == pivot:
                equal_to_pivot.append(num)
            else:
                greater_than_pivot.append(num)

        # Concatenate the three lists
        return less_than_pivot + equal_to_pivot + greater_than_pivot
