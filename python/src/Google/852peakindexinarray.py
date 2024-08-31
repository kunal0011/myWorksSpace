class Solution:
    def peakIndexInMountainArray(self, arr):
        low, high = 0, len(arr) - 1

        while low < high:
            mid = (low + high) // 2
            if arr[mid] < arr[mid + 1]:
                # Peak is to the right of mid
                low = mid + 1
            else:
                # Peak is to the left of mid, or it is mid
                high = mid

        return low


# Example usage
arr = [0, 2, 4, 7, 6, 3, 1]
solution = Solution()
peak_index = solution.peakIndexInMountainArray(arr)
print(peak_index)  # Output: 3
