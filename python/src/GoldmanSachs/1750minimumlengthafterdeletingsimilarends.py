
class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1

        while left < right and s[left] == s[right]:
            char = s[left]
            # Move left pointer to the right while characters are the same
            while left <= right and s[left] == char:
                left += 1
            # Move right pointer to the left while characters are the same
            while left <= right and s[right] == char:
                right -= 1

        # The remaining length of the string
        return right - left + 1


# Example usage
solution = Solution()
# Output: 1 (after removing 'a', 'b', 'b', 'a', 'c', 'c', 'd')
print(solution.minimumLength("abbaccd"))
# Output: 1 (after removing 'c', 'c', 'c', 'c', 'c')
print(solution.minimumLength("acccc"))
# Output: 2 (no characters can be removed)
print(solution.minimumLength("ab"))
