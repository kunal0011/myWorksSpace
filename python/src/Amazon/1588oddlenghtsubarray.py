class Solution:
    def sumOddLengthSubarrays(self, arr):
        total_sum = 0
        n = len(arr)

        # Iterate through each element
        for i in range(n):
            # Calculate contribution of arr[i] to all odd-length subarrays
            left = i + 1  # Number of subarrays ending at or before index i
            right = n - i  # Number of subarrays starting at or after index i

            # Total subarrays that include arr[i]
            total_subarrays = left * right

            # Odd-length subarrays that include arr[i]
            odd_subarrays = (total_subarrays + 1) // 2

            # Add the contribution of arr[i] to the total sum
            total_sum += odd_subarrays * arr[i]

        return total_sum


# Testing
solution = Solution()
arr = [1, 4, 2, 5, 3]
# Output should be 58
print("Python Test Result:", solution.sumOddLengthSubarrays(arr))
