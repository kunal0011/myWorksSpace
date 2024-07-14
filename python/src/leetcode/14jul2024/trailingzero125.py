class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n >= 5:
            n //= 5
            count += n
        return count

# Example usage:
# sol = Solution()
# print(sol.trailingZeroes(5))    # Output: 1
# print(sol.trailingZeroes(10))   # Output: 2
# print(sol.trailingZeroes(25))   # Output: 6
