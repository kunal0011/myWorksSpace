from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # Step 1: Sort the array and store the index of each element
        sorted_nums = sorted(nums)

        # Step 2: Create a dictionary to store how many numbers are smaller than each number
        num_to_count = {}

        # Store the index (i.e., how many numbers are smaller) for the first occurrence of each number
        for i, num in enumerate(sorted_nums):
            if num not in num_to_count:
                num_to_count[num] = i

        # Step 3: Use the dictionary to create the result array
        result = [num_to_count[num] for num in nums]
        return result


# Testing
solution = Solution()
nums = [8, 1, 2, 2, 3]
# Output: [4, 0, 1, 1, 3]
print("Python Test Result:", solution.smallerNumbersThanCurrent(nums))
