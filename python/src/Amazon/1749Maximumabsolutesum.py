class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        max_sum = 0
        min_sum = 0
        current_max = 0
        current_min = 0

        for num in nums:
            current_max = max(current_max + num, num)
            max_sum = max(max_sum, current_max)

            current_min = min(current_min + num, num)
            min_sum = min(min_sum, current_min)

        return max(abs(max_sum), abs(min_sum))


# Testing the solution
if __name__ == "__main__":
    solution = Solution()

    # Test case
    nums = [1, -3, 2, 3, -4]
    # Expected output: 5
    print("Maximum absolute sum:", solution.maxAbsoluteSum(nums))
