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
