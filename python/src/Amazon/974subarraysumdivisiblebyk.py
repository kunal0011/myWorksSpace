from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], K: int) -> int:
        # Hashmap to store remainder frequencies
        remainder_count = {0: 1}

        prefix_sum = 0  # To store the running prefix sum
        result = 0      # To store the number of valid subarrays

        # Iterate through each number in the array
        for num in nums:
            # Update the prefix sum
            prefix_sum += num

            # Compute the remainder of the current prefix sum mod K
            remainder = prefix_sum % K

            # If remainder is negative, convert it to positive
            if remainder < 0:
                remainder += K

            # If this remainder has been seen before, we can form subarrays
            if remainder in remainder_count:
                result += remainder_count[remainder]

            # Update the frequency of the current remainder
            remainder_count[remainder] = remainder_count.get(remainder, 0) + 1

        return result
