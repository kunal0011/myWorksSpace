class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = {'a': 0, 'b': 0, 'c': 0}
        left = 0
        result = 0
        n = len(s)

        for right in range(n):
            count[s[right]] += 1

            while all(count[char] > 0 for char in 'abc'):
                # All characters are present in the window [left:right+1]
                result += n - right  # All substrings starting from current `left` to the end of string
                count[s[left]] -= 1
                left += 1

        return result


# Example usage:
sol = Solution()
s1 = "abcabc"
print(sol.numberOfSubstrings(s1))  # Output: 10

s2 = "aaacb"
print(sol.numberOfSubstrings(s2))  # Output: 3

s3 = "abc"
print(sol.numberOfSubstrings(s3))  # Output: 1
