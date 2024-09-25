from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sequential_nums = []

        # Generate sequential digits
        for start in range(1, 10):  # Starting digits from 1 to 9
            num = start
            next_digit = start

            while next_digit < 9:  # Generate sequential numbers
                next_digit += 1
                num = num * 10 + next_digit

                # Add to list if within range
                if low <= num <= high:
                    sequential_nums.append(num)

        # Return sorted results
        return sorted(sequential_nums)
