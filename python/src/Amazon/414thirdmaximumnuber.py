class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        distinct_nums = set(nums)

        if len(distinct_nums) < 3:
            return max(distinct_nums)

        distinct_nums.remove(max(distinct_nums))  # Remove the largest
        distinct_nums.remove(max(distinct_nums))  # Remove the second largest

        return max(distinct_nums)  # Return the third largest


# Example usage:
solution = Solution()
print(solution.thirdMax([3, 2, 1]))  # Expected output: 1
print(solution.thirdMax([1, 2]))     # Expected output: 2
print(solution.thirdMax([2, 2, 3, 1]))  # Expected output: 1
