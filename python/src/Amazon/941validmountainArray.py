class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        if len(arr) < 3:
            return False

        # Find the peak
        i = 0
        # Climb up to the peak
        while i + 1 < len(arr) and arr[i] < arr[i + 1]:
            i += 1

        # If we never climbed or we are at the last element, it's not a mountain
        if i == 0 or i == len(arr) - 1:
            return False

        # Climb down from the peak
        while i + 1 < len(arr) and arr[i] > arr[i + 1]:
            i += 1

        # Check if we've reached the end of the array
        return i == len(arr) - 1


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    arr1 = [2, 1]
    print(sol.validMountainArray(arr1))  # Expected output: False

    # Test case 2
    arr2 = [3, 5, 5]
    print(sol.validMountainArray(arr2))  # Expected output: False

    # Test case 3
    arr3 = [0, 3, 2, 1]
    print(sol.validMountainArray(arr3))  # Expected output: True
