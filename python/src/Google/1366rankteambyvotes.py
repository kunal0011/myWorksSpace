"""
LeetCode 1366: Rank Teams by Votes

Problem Statement:
In a special ranking system, each voter gives a rank from highest to lowest to all teams.
The ordering of teams is decided by who received the most position-one votes. 
If two or more teams tie in position-one votes, we consider position-two votes and so on.
If two teams are still tied after considering all positions, we break the tie alphabetically based on team letter.

Logic:
1. Create a rank count dictionary where:
   - Key: team letter
   - Value: list of counts for each position
2. For each vote and position:
   - Increment count for that team at that position
3. Sort teams based on:
   - Primary: Their position counts (higher is better)
   - Secondary: Team letter (alphabetically) for ties
4. Join sorted teams into final string

Time Complexity: O(N * M * log(M)) where:
- N is number of votes
- M is number of teams
Space Complexity: O(M) for rank count dictionary
"""

from collections import defaultdict


class Solution:
    def rankTeams(self, votes: list[str]) -> str:
        # Number of teams
        n = len(votes[0])

        # Create a dictionary where each team points to a list of size n
        rank_count = defaultdict(lambda: [0] * n)

        # Tally the votes
        for vote in votes:
            for i, team in enumerate(vote):
                rank_count[team][i] += 1

        # Sort the teams based on the rank counts and alphabetically for ties
        sorted_teams = sorted(rank_count.keys(), key=lambda team: (
            rank_count[team], -ord(team)), reverse=True)

        # Join the sorted teams into a string and return
        return ''.join(sorted_teams)


def test_rank_teams():
    solution = Solution()

    # Test case 1: Basic ranking
    votes1 = ["ABC", "ACB", "ABC", "ACB", "ACB"]
    result1 = solution.rankTeams(votes1)
    assert result1 == "ACB", f"Test case 1 failed. Expected 'ACB', got {result1}"
    print(f"Test case 1 passed: {result1}")

    # Test case 2: All teams tied
    votes2 = ["WXYZ", "XYZW"]
    result2 = solution.rankTeams(votes2)
    assert result2 == "WXYZ", f"Test case 2 failed. Expected 'WXYZ', got {result2}"
    print(f"\nTest case 2 passed: {result2}")

    # Test case 3: Single vote
    votes3 = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]
    result3 = solution.rankTeams(votes3)
    assert result3 == "ZMNAGUEDSJYLBOPHRQICWFXTVK", \
        f"Test case 3 failed. Expected 'ZMNAGUEDSJYLBOPHRQICWFXTVK', got {result3}"
    print(f"\nTest case 3 passed: {result3}")

    # Test case 4: Two teams only
    votes4 = ["AB", "BA", "AB"]
    result4 = solution.rankTeams(votes4)
    assert result4 == "AB", f"Test case 4 failed. Expected 'AB', got {result4}"
    print(f"\nTest case 4 passed: {result4}")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_rank_teams()
