from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd_count = 0
        # Initialize with 1 for the case where prefix sum is even initially (like sum = 0)
        even_count = 1
        prefix_sum = 0
        result = 0
        MOD = 10**9 + 7

        for num in arr:
            # Update the prefix sum
            prefix_sum += num

            # Check if the prefix sum is odd or even
            if prefix_sum % 2 == 0:
                # If prefix_sum is even, add the odd_count subarrays
                result += odd_count
                even_count += 1
            else:
                # If prefix_sum is odd, add the even_count subarrays
                result += even_count
                odd_count += 1

            # Since the result can be large, take modulo MOD
            result %= MOD

        return result
