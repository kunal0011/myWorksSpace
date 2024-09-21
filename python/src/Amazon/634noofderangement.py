class Solution:
    def findDerangement(self, n: int) -> int:
        MOD = 10**9 + 7

        if n == 1:
            return 0
        if n == 2:
            return 1

        # Initialize base cases
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: D(0) = 1 (by convention)
        dp[1] = 0  # Base case: D(1) = 0

        # Fill the dp array using the recurrence relation
        for i in range(2, n + 1):
            dp[i] = (i - 1) * (dp[i - 1] + dp[i - 2]) % MOD

        return dp[n]


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    n1 = 3
    print(sol.findDerangement(n1))  # Output: 2

    # Test case 2
    n2 = 2
    print(sol.findDerangement(n2))  # Output: 1

    # Test case 3
    n3 = 4
    print(sol.findDerangement(n3))  # Output: 9
