from typing import List


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        total_shift = 0
        length = len(s)

        # Calculate net shift value
        for amount, direction in shift:
            if direction == 1:
                total_shift += amount
            else:
                total_shift -= amount

        # Normalize total_shift to be within the range of the string length
        total_shift = total_shift % length

        # Perform the shift
        if total_shift < 0:
            total_shift += length

        return s[-total_shift:] + s[:-total_shift]
