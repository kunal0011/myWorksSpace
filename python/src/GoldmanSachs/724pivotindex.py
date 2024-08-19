class Solution:
    def pivotIndex(self, nums):
        total_sum = sum(nums)
        prefix_sum = 0

        for i, num in enumerate(nums):
            # Calculate right sum by subtracting the prefix sum and current element from total sum
            right_sum = total_sum - prefix_sum - num
            if prefix_sum == right_sum:
                return i
            prefix_sum += num

        return -1


# Example usage
solution = Solution()
print(solution.pivotIndex([1, 7, 3, 6, 5, 6]))  # Output: 3
print(solution.pivotIndex([1, 2, 3]))           # Output: -1
print(solution.pivotIndex([2, 1, -1]))          # Output: 0
