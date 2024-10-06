from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Initialize the maximum, minimum products and result with the first element
        max_prod = min_prod = result = nums[0]

        # Iterate through the array starting from the second element
        for num in nums[1:]:
            if num < 0:
                # Swap max_prod and min_prod when a negative number is encountered
                max_prod, min_prod = min_prod, max_prod

            # Update max_prod and min_prod
            max_prod = max(num, max_prod * num)
            min_prod = min(num, min_prod * num)

            # Update the result with the current max_prod
            result = max(result, max_prod)

        return result
