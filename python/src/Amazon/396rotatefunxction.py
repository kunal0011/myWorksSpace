class Solution:
    def maxRotateFunction(self, nums):
        n = len(nums)
        total_sum = sum(nums)
        # Compute F(0)
        F_0 = sum(i * nums[i] for i in range(n))

        # Initialize current F and max_value with F(0)
        max_value = F_0
        current_F = F_0

        # Compute subsequent F(k) for k = 1 to n-1
        for k in range(1, n):
            current_F += total_sum - n * nums[n - k]
            max_value = max(max_value, current_F)

        return max_value


# Test the solution
if __name__ == "__main__":
    sol = Solution()

    # Test case 1: Example from Leetcode
    nums = [4, 3, 2, 6]
    print(sol.maxRotateFunction(nums))  # Expected output: 26

    # Test case 2: All elements are the same
    nums = [100, 100, 100]
    print(sol.maxRotateFunction(nums))  # Expected output: 0

    # Test case 3: Array of length 1
    nums = [1]
    print(sol.maxRotateFunction(nums))  # Expected output: 0
