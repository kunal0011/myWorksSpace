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


# Example usage:
sol = Solution()
print(sol.maxProduct([2, 3, -2, 4]))  # Output: 6 (subarray [2, 3])
print(sol.maxProduct([-2, 0, -1]))    # Output: 0 (subarray [0])
print(sol.maxProduct([-2, 3, -4]))    # Output: 24 (subarray [3, -4])
print(sol.maxProduct([0, 2]))         # Output: 2 (subarray [2])
print(sol.maxProduct([-2, -3, -4]))   # Output: 12 (subarray [-2, -3, -4])
