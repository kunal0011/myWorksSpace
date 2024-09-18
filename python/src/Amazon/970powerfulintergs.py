from typing import List


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        result = set()

        # Iterate through powers of x
        i = 0
        while x**i <= bound:
            j = 0
            while y**j <= bound:
                powerful_int = x**i + y**j
                if powerful_int <= bound:
                    result.add(powerful_int)
                j += 1
                if y == 1:
                    break  # Stop if y is 1 to avoid infinite loop
            i += 1
            if x == 1:
                break  # Stop if x is 1 to avoid infinite loop

        return list(result)


# Testing
solution = Solution()
x = 2
y = 3
bound = 10
print("Python Test Result:", solution.powerfulIntegers(
    x, y, bound))  # Output: [2, 3, 4, 5, 7, 9, 10]
