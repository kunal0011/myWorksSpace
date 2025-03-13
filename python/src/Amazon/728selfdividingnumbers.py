"""
LeetCode 728: Self Dividing Numbers

A self-dividing number is a number that is divisible by every digit it contains.
- For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
- A self-dividing number is not allowed to contain the digit zero.

Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].
"""

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        # Time Complexity: O(n * d) where n is range size and d is average number of digits
        # Space Complexity: O(1) excluding output array
        def is_self_dividing(n: int) -> bool:
            num = n
            while num:
                digit = num % 10
                if digit == 0 or n % digit != 0:
                    return False
                num //= 10
            return True

        return [num for num in range(left, right + 1) if is_self_dividing(num)]

def test_self_dividing_numbers():
    """Test function with multiple test cases"""
    test_cases = [
        (1, 22, [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]),
        (47, 85, [48, 55, 66, 77]),
        (1, 10, [1, 2, 3, 4, 5, 6, 7, 8, 9]),
        (100, 120, [111, 112, 115, 120])
    ]
    
    solution = Solution()
    for i, (left, right, expected) in enumerate(test_cases, 1):
        result = solution.selfDividingNumbers(left, right)
        success = result == expected
        print(f"\nTest case {i}:")
        print(f"Input: left = {left}, right = {right}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"{'✓ Passed' if success else '✗ Failed'}")

if __name__ == "__main__":
    test_self_dividing_numbers()
