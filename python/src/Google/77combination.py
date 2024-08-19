from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start, current):
            if len(current) == k:
                # make a copy of current and append to result
                result.append(current[:])
                return
            for i in range(start, n + 1):
                current.append(i)
                backtrack(i + 1, current)
                current.pop()

        result = []
        backtrack(1, [])
        return result
