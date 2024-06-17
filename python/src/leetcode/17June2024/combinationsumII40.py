from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def backtrack(start, remain, current):
            if remain == 0:
                result.append(current[:])
                return
            elif remain < 0:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                current.append(candidates[i])
                backtrack(i+1, remain - candidates[i], current)
                current.pop()

        backtrack(0, target, [])
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum2([2, 3, 6, 7], 7))
    print(s.combinationSum2([2, 3, 5], 8))
    print(s.combinationSum2([2], 1))
    print(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
    print(s.combinationSum2([2, 5, 2, 1, 2], 5))
