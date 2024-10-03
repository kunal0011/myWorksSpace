class Solution:
    def plusOne(self, digits):
        n = len(digits)

        # Start from the last digit
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0

        # If all digits are 9, the number will become 100...0
        return [1] + digits


# Example usage
solution = Solution()
digits = [1, 2, 3]
print(solution.plusOne(digits))  # Output: [1, 2, 4]

digits = [9, 9, 9]
print(solution.plusOne(digits))  # Output: [1, 0, 0, 0]
