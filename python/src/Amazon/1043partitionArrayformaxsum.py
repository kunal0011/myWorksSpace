class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        n = len(arr)
        dp = [0] * n

        # Loop through each index of the array
        for i in range(n):
            max_val = 0
            # Try to form subarrays of length 1 to k ending at index i
            for j in range(1, min(k, i+1) + 1):
                # Maximum value in the subarray of length j
                max_val = max(max_val, arr[i - j + 1])
                if i >= j:
                    dp[i] = max(dp[i], dp[i - j] + max_val * j)
                else:
                    dp[i] = max(dp[i], max_val * j)

        return dp[-1]

# Testing the implementation


def test_max_sum_after_partitioning():
    solution = Solution()

    # Test case 1
    arr1 = [1, 15, 7, 9, 2, 5, 10]
    k1 = 3
    # Expected output: 84 (Partition: [15,15,15], [9], [10,10])
    result1 = solution.maxSumAfterPartitioning(arr1, k1)
    print(f"Test 1 - Result: {result1}, Expected: 84")

    # Test case 2
    arr2 = [1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3]
    k2 = 4
    # Expected output: 83 (Partition: [4,4,5,7], [7,7,7], [9,9], [9])
    result2 = solution.maxSumAfterPartitioning(arr2, k2)
    print(f"Test 2 - Result: {result2}, Expected: 83")

    # Test case 3
    arr3 = [1]
    k3 = 1
    # Expected output: 1 (Only one element, so no partitioning needed)
    result3 = solution.maxSumAfterPartitioning(arr3, k3)
    print(f"Test 3 - Result: {result3}, Expected: 1")


# Run the test
test_max_sum_after_partitioning()
