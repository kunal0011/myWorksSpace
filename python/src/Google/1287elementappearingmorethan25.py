class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        n = len(arr)
        threshold = n // 4

        # Iterate through the array and check for frequency
        i = 0
        while i < n:
            count = 1
            # Count the number of times arr[i] appears consecutively
            while i + 1 < n and arr[i] == arr[i + 1]:
                count += 1
                i += 1

            if count > threshold:
                return arr[i]

            i += 1

        return -1
