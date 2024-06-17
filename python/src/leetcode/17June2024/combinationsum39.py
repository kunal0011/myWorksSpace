from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.li = []

        def process_combination_sum(candidates1: List[int], target1: int, proceesed: List[int]) -> None:

            if target1 == 0:
                self.li.append(proceesed[:])
                return None

            if target1 < 0 or len(candidates1) == 0:
                return None

            proceesed.append(candidates1[0])
            process_combination_sum(
                candidates1, target1-candidates1[0], proceesed)
            proceesed.pop()
            process_combination_sum(candidates1[1:], target1, proceesed)
        process_combination_sum(candidates, target, [])
        return self.li


class Solution1:
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


if __name__ == '__main__':
    s = Solution1()
    print(s.combinationSum([2, 3, 6, 7], 7))
    print(s.combinationSum([2, 3, 5], 8))
    print(s.combinationSum([2], 1))
