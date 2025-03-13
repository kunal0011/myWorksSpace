"""
LeetCode 670: Maximum Swap

Problem Statement:
You are given an integer num. You can swap two digits at most once to get the maximum valued number.
Return the maximum valued number you can get.

Key Points:
1. We can only perform at most one swap
2. We need to find the maximum possible value after one swap
3. The number remains the same if no swap improves it
"""

class Solution:
    def maximumSwap(self, num: int) -> int:
        # Convert number to list of digits for easy manipulation
        digits = list(str(num))
        n = len(digits)
        
        # Store last occurrence of each digit
        last_pos = {int(d): i for i, d in enumerate(digits)}
        
        # Check each position from left to right
        for i in range(n):
            current_digit = int(digits[i])
            # Try to swap with largest possible digit that comes later
            for d in range(9, current_digit, -1):
                if d in last_pos and last_pos[d] > i:
                    # Swap the digits
                    digits[i], digits[last_pos[d]] = digits[last_pos[d]], digits[i]
                    return int(''.join(digits))
        
        return num

def test_maximum_swap():
    solution = Solution()
    
    # Test cases: (input_num, expected_output, description)
    test_cases = [
        (2736, 7236, "Basic case - swap first and second digits"),
        (9973, 9973, "Already maximum number"),
        (98368, 98863, "Swap digits in middle"),
        (1993, 9913, "Swap with leading digit"),
        (1234, 4231, "Swap first and last digits"),
        (10, 10, "Two digit number, no improvement"),
        (1, 1, "Single digit"),
        (99901, 99910, "Multiple same digits"),
        (12121, 21121, "Repeated digits"),
    ]
    
    for i, (num, expected, description) in enumerate(test_cases, 1):
        result = solution.maximumSwap(num)
        assert result == expected, \
            f"Test {i} failed: {description}\nExpected {expected}, got {result}"
        print(f"Test {i} passed: {description}")
        print(f"Input: {num}")
        print(f"Output: {result}")
        print("-" * 50)

if __name__ == "__main__":
    test_maximum_swap()
