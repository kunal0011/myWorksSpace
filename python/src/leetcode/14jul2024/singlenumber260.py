from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_result = 0
        for num in nums:
            xor_result ^= num

        # Step 2: Find any bit that is set in xor_result
        # We choose the rightmost set bit for simplicity
        bitmask = xor_result & (-xor_result)

        # Step 3: Initialize two variables to store the two unique numbers
        num1 = 0
        num2 = 0

        # Step 4: Partition the array into two groups based on the bitmask
        for num in nums:
            if num & bitmask:
                num1 ^= num  # XOR of all numbers where the bitmask bit is set
            else:
                num2 ^= num  # XOR of all numbers where the bitmask bit is not set

        return [num1, num2]
