import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # Initialize two pointers
        a = 0
        b = int(math.sqrt(c))  # b starts from the square root of c

        # Use two pointers to check if a^2 + b^2 = c
        while a <= b:
            sum_of_squares = a * a + b * b
            if sum_of_squares == c:
                return True
            elif sum_of_squares < c:
                a += 1
            else:
                b -= 1

        return False


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    c1 = 5
    print(sol.judgeSquareSum(c1))  # Output: True

    # Test case 2
    c2 = 3
    print(sol.judgeSquareSum(c2))  # Output: False

    # Test case 3
    c3 = 4
    print(sol.judgeSquareSum(c3))  # Output: True
