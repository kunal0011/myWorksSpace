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
