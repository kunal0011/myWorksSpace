class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        # Sort the array
        arr.sort()

        # Get the difference between the first two elements
        diff = arr[1] - arr[0]

        # Check if the difference is consistent for all pairs
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != diff:
                return False

        return True
