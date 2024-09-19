class Solution:
    def numFactoredBinaryTrees(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        arr.sort()
        dp = {}

        for num in arr:
            # Every number can form at least one tree with itself as the root.
            dp[num] = 1

        for i in range(len(arr)):
            for j in range(i):
                if arr[i] % arr[j] == 0:  # arr[i] = arr[j] * another number
                    right = arr[i] // arr[j]
                    if right in dp:
                        dp[arr[i]] = (dp[arr[i]] + dp[arr[j]]
                                      * dp[right]) % MOD

        return sum(dp.values()) % MOD


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    arr1 = [2, 4]
    print(sol.numFactoredBinaryTrees(arr1))  # Expected output: 3

    # Test case 2
    arr2 = [2, 4, 5, 10]
    print(sol.numFactoredBinaryTrees(arr2))  # Expected output: 7
