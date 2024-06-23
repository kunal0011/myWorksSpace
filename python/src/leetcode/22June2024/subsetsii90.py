from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            # Append a copy of the current path (subset) to the result
            result.append(path[:])
            # Explore further elements to include in the subset
            for i in range(start, len(nums)):
                # If the current element is the same as the previous element, skip it to avoid duplicates
                if i > start and nums[i] == nums[i - 1]:
                    continue
                # Include the current element and move to the next element
                path.append(nums[i])
                backtrack(i + 1, path)
                # Exclude the current element (backtrack)
                path.pop()

    # Sort the array to handle duplicates
        nums.sort()
        result = []
        backtrack(0, [])
        return result


s = Solution()
nums = [1, 2, 2]
print("All possible subsets without duplicates:")
print(s.subsetsWithDup(nums))
