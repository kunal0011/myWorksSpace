class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        n = len(arr)
        if n < k:
            return 0

        # Calculate the initial sum of the first window of size k
        current_sum = sum(arr[:k])
        count = 0

        # Check if the average of the first window meets the threshold
        if current_sum / k >= threshold:
            count += 1

        # Slide the window across the array
        for i in range(k, n):
            # Update the sum by subtracting the element that is leaving the window
            # and adding the element that is entering the window
            current_sum = current_sum - arr[i - k] + arr[i]

            # Check if the average of the current window meets the threshold
            if current_sum / k >= threshold:
                count += 1

        return count


sol = Solution()
# Example usage:
arr1 = [2, 1, 3, 4, 5]
k1 = 3
threshold1 = 4
print(sol.numOfSubarrays(arr1, k1, threshold1))  # Output: 3

arr2 = [1, 1, 1, 1, 1]
k2 = 1
threshold2 = 0
print(sol.numOfSubarrays(arr2, k2, threshold2))  # Output: 5

arr3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k3 = 3
threshold3 = 5
print(sol.numOfSubarrays(arr3, k3, threshold3))  # Output: 6

arr4 = [4, 4, 4, 4]
k4 = 4
threshold4 = 1
print(sol.numOfSubarrays(arr4, k4, threshold4))  # Output: 1
