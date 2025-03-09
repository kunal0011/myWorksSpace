class Solution:
    def isHappy(self, n: int) -> bool:
        # Helper function to get the next number in the sequence
        def get_next_number(n):
            total_sum = 0
            while n > 0:
                digit = n % 10
                total_sum += digit ** 2
                n //= 10
            return total_sum

        # Using a set to detect cycles
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next_number(n)

        return n == 1

# Problem Statement:
# Write an algorithm to determine if a number n is happy.
# A happy number is a number defined by the following process:
# - Starting with any positive integer, replace the number by the sum of the squares of its digits.
# - Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# - Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

# Sample Example:
# Input: 19
# Output: true
# Explanation: 
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1

# Test driver program
if __name__ == "__main__":
    solution = Solution()
    test_cases = [19, 2, 7, 20]
    for num in test_cases:
        print(f"Is {num} a happy number? {solution.isHappy(num)}")
