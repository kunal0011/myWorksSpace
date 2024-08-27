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
