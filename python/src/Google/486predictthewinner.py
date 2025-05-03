"""
LeetCode 486 - Predict the Winner

Problem Statement:
You are given an integer array nums. Two players are playing a game with this array: player 1 and player 2.
Player 1 and player 2 take turns, with player 1 starting first. Both players start the game with a score of 0. 
At each turn, the player takes one of the numbers from either end of the array (first or last element) which adds to their score.
The game ends when there are no more elements in the array.
Return true if Player 1 can win the game. If the scores are equal, Player 1 still wins.

Example:
Input: nums = [1,5,2]
Output: false
Explanation: Initially, player 1 can choose between 1 and 2. 
If player 1 chooses 2, then player 2 can choose from 1 and 5. If player 2 chooses 5, then player 1 will be left with 1.
So final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
Hence, player 1 will never be the winner and returns false.

Time Complexity: O(n^2) where n is the length of the array
Space Complexity: O(n^2) for the dynamic programming table
"""


def predict_the_winner(nums: list[int]) -> bool:
    n = len(nums)
    # dp[i][j] represents the maximum score difference (player1 - player2)
    # that player 1 can achieve from index i to j
    dp = [[0] * n for _ in range(n)]

    # Base case: single numbers
    for i in range(n):
        dp[i][i] = nums[i]

    # Fill the dp table
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            # Choose first number minus opponent's best choice
            take_first = nums[i] - dp[i + 1][j]
            # Choose last number minus opponent's best choice
            take_last = nums[j] - dp[i][j - 1]
            dp[i][j] = max(take_first, take_last)

    # If final score difference ≥ 0, player 1 wins
    return dp[0][n-1] >= 0

# Test driver


def run_tests():
    test_cases = [
        ([1, 5, 2], False),
        ([1, 5, 233, 7], True),
        ([1, 2, 3, 4], True),
        ([1, 1], True),
        ([1], True)
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        result = predict_the_winner(nums)
        status = "✓" if result == expected else "✗"
        print(f"Test {i}: {status}")
        print(f"Input: {nums}")
        print(f"Expected: {expected}")
        print(f"Got: {result}\n")


if __name__ == "__main__":
    run_tests()
