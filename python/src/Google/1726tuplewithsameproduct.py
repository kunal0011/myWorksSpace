"""
LeetCode 1726. Tuple with Same Product

Problem Statement:
Given an array nums of distinct positive integers, return the number of tuples (a,b,c,d) such that
a * b = c * d where a, b, c, and d are elements of nums, and a != b != c != d.

Time Complexity: O(n^2) where n is length of array
Space Complexity: O(n^2) to store products
"""

from typing import List
from collections import defaultdict


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        # Logic:
        # 1. For each pair of numbers (a,b), calculate their product
        # 2. Keep count of each product in a hash map
        # 3. For each product with count > 1:
        #    - Calculate number of valid pairs that give same product
        #    - Each valid pair can form 8 different tuples (permutations)
        # 4. Return total count * 8

        product_count = defaultdict(int)

        # Calculate all possible products and store their frequencies
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                product_count[product] += 1

        # Calculate the number of valid tuples based on the frequency of products
        result = 0
        for count in product_count.values():
            if count > 1:
                # For each pair of pairs with same product
                # C(count,2) = count * (count-1) / 2
                result += count * (count - 1) // 2

        # Each valid product combination contributes 8 tuples
        # (a,b,c,d), (a,b,d,c), (b,a,c,d), (b,a,d,c)
        # (c,d,a,b), (c,d,b,a), (d,c,a,b), (d,c,b,a)
        return result * 8


# Test driver
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        [2, 3, 4, 6],          # Expected: 8
        [1, 2, 4, 5, 10],       # Expected: 16
        [2, 3, 4, 6, 8, 12],     # Expected: 40
        [1, 2, 3, 4, 5],        # Expected: 0
    ]

    for i, nums in enumerate(test_cases):
        result = solution.tupleSameProduct(nums)
        print(f"Test case {i + 1}:")
        print(f"Input array: {nums}")
        print(f"Number of valid tuples: {result}")

        # Print some valid tuples for verification (if any exist)
        if result > 0:
            print("Example valid tuples:")
            found = set()
            for a in range(len(nums)):
                for b in range(a + 1, len(nums)):
                    for c in range(b + 1, len(nums)):
                        for d in range(c + 1, len(nums)):
                            if (nums[a] * nums[b] == nums[c] * nums[d] and
                                    len({nums[a], nums[b], nums[c], nums[d]}) == 4):
                                print(
                                    f"({nums[a]},{nums[b]},{nums[c]},{nums[d]})")
                                found.add((nums[a], nums[b], nums[c], nums[d]))
                                if len(found) >= 3:  # Show at most 3 examples
                                    break
                        if len(found) >= 3:
                            break
                    if len(found) >= 3:
                        break
                if len(found) >= 3:
                    break
        print()
