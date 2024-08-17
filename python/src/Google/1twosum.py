from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store the index of the required difference
        num_to_index = {}

        # Iterate through the list
        for i, num in enumerate(nums):
            # Calculate the difference
            difference = target - num

            # If the difference exists in the dictionary, return the indices
            if difference in num_to_index:
                return [num_to_index[difference], i]

            # Otherwise, store the current number and its index
            num_to_index[num] = i


# Example usage:
if __name__ == "__main__":
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(solution.twoSum(nums, target))  # Output: [0, 1]
