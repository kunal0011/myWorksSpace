class Solution:
    def increasingTriplet(self, nums):
        # Initialize the first and second smallest numbers
        first = float('inf')
        second = float('inf')

        # Iterate through the array
        for num in nums:
            if num <= first:
                # Update the smallest number
                first = num
            elif num <= second:
                # Update the second smallest number
                second = num
            else:
                # If we find a number greater than both first and second, return True
                return True

        # If no such triplet is found, return False
        return False
