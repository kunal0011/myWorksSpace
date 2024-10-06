from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, remain, current):
            if remain == 0:
                result.append(current[:])
                return
            elif remain < 0:
                return

            for i in range(start, len(candidates)):
                current.append(candidates[i])
                backtrack(i, remain - candidates[i], current)
                current.pop()

        backtrack(0, target, [])
        return result
