class Solution:
    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        def backtrack(start, path):
            if len(path) > 1:
                # Convert list to tuple to use in a set
                result.add(tuple(path))
            used = set()  # To avoid using the same element in the same position
            for i in range(start, len(nums)):
                if nums[i] in used:
                    continue
                if not path or nums[i] >= path[-1]:
                    used.add(nums[i])
                    backtrack(i + 1, path + [nums[i]])

        result = set()
        backtrack(0, [])
        return [list(seq) for seq in result]
