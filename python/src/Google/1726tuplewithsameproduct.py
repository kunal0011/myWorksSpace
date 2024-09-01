from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        from collections import defaultdict

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
                result += count * (count - 1) // 2

        # Each valid product combination contributes 8 tuples
        return result * 8
