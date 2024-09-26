class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7

        # Define the valid moves for each digit
        moves = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],      # No moves for 5
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }

        # Initialize dp arrays
        # Base case: n = 1, each number can only dial itself
        dp_prev = [1] * 10
        dp_curr = [0] * 10  # To store results for the next length

        # Perform the DP update for each length from 2 to n
        for _ in range(1, n):
            for digit in range(10):
                dp_curr[digit] = 0  # Reset current digit count
                for next_digit in moves[digit]:
                    dp_curr[digit] = (
                        dp_curr[digit] + dp_prev[next_digit]) % MOD

            # Move dp_curr to dp_prev for the next iteration
            dp_prev, dp_curr = dp_curr, dp_prev

        # Sum all valid counts for the last digit configuration
        return sum(dp_prev) % MOD
