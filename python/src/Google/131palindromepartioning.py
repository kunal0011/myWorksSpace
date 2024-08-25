from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(string):
            return string == string[::-1]

        def backtrack(start, current_partition):
            if start == len(s):
                result.append(current_partition[:])
                return

            for i in range(start, len(s)):
                substring = s[start:i+1]
                if isPalindrome(substring):
                    current_partition.append(substring)
                    backtrack(i + 1, current_partition)
                    current_partition.pop()

        result = []
        backtrack(0, [])
        return result
