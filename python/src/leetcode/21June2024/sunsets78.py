from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, current):
            # Add the current subset to the result
            result.append(current[:])

            # Iterate over remaining elements to explore further subsets
            for i in range(start, len(nums)):
                current.append(nums[i])
                # Recursively backtrack with the next starting index
                backtrack(i + 1, current)
                # Backtrack: remove the last added element to explore other subsets
                current.pop()

        result = []
        backtrack(0, [])
        return result


# Example usage:
solution = Solution()
nums = [1, 2, 3]
print(solution.subsets(nums))
