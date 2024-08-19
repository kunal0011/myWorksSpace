class Solution:
    def twoSum(self, nums, target):
        # Create a hash map to store the number and its index
        num_to_index = {}

        for index, num in enumerate(nums):
            # Calculate the complement of the current number
            complement = target - num

            # Check if the complement exists in the hash map
            if complement in num_to_index:
                # Return the indices of the two numbers
                return [num_to_index[complement], index]

            # Store the index of the current number
            num_to_index[num] = index

        # If no solution is found, though the problem guarantees one solution
        return []


# Example usage
solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(solution.twoSum([3, 2, 4], 6))        # Output: [1, 2]
print(solution.twoSum([3, 3], 6))           # Output: [0, 1]
