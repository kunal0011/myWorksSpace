from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # Start checking from 1
        missing_count = 0
        current = 1
        idx = 0

        # Iterate while we haven't found the kth missing number
        while k > 0:
            # If the current number is not in the array, it's missing
            if idx >= len(arr) or arr[idx] != current:
                missing_count += 1
                # If this is the kth missing number, return it
                if missing_count == k:
                    return current
            else:
                idx += 1
            current += 1

        # Return the kth missing positive number
        return current
