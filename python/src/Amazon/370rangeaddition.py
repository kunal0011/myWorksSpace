from typing import List


class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        # Step 1: Initialize the result array with zeros
        result = [0] * length

        # Step 2: Apply each update operation efficiently
        for update in updates:
            start, end, inc = update
            result[start] += inc
            if end + 1 < length:
                result[end + 1] -= inc

        # Step 3: Compute the cumulative sum to get the final result
        for i in range(1, length):
            result[i] += result[i - 1]

        return result
