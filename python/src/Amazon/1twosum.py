# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]


# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
class Solution:
    def twoSum(self, nums, target):
        # Dictionary to store the value and its index
        lookup = {}

        # Iterate over the list of numbers
        for i, num in enumerate(nums):
            # Calculate the complement
            complement = target - num

            # If complement exists in the lookup dictionary, return the indices
            if complement in lookup:
                return [lookup[complement], i]

            # Store the index of the current number in the dictionary
            lookup[num] = i


def test_twoSum():
    solution = Solution()

    # Test case 1
    nums = [2, 7, 11, 15]
    target = 9
    assert solution.twoSum(nums, target) == [0, 1], "Test case 1 failed"

    # Test case 2
    nums = [3, 2, 4]
    target = 6
    assert solution.twoSum(nums, target) == [1, 2], "Test case 2 failed"

    # Test case 3
    nums = [3, 3]
    target = 6
    assert solution.twoSum(nums, target) == [0, 1], "Test case 3 failed"

    print("All test cases passed!")


# Run the test cases
test_twoSum()
