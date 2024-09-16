class Solution:
    def findKthPositive(self, arr, k):
        missing_count = 0
        current_num = 1
        index = 0

        while missing_count < k:
            # If current_num is in arr, skip it
            if index < len(arr) and arr[index] == current_num:
                index += 1
            else:
                # Otherwise, it's a missing number
                missing_count += 1
            # Move to the next number
            current_num += 1

        # Since we overshoot by one in the last iteration
        return current_num - 1


# Testing
solution = Solution()
arr = [2, 3, 4, 7, 11]
k = 5
print("Python Test Result:", solution.findKthPositive(
    arr, k))  # Output should be 9
