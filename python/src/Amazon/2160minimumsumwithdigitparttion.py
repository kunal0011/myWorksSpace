class Solution:
    def minimumSum(self, num: int) -> int:
        digits = [int(d) for d in str(num)]  # Extract digits
        digits.sort()  # Sort digits to easily find minimal combinations

        # Form two smallest and two largest possible two-digit numbers
        num1 = digits[0] * 10 + digits[1]
        num2 = digits[2] * 10 + digits[3]

        return min(num1 + num2,
                   digits[0] * 10 + digits[2] + digits[1] * 10 + digits[3])


# Example usage
sol = Solution()
print(sol.minimumSum(2932))  # Output: 52
