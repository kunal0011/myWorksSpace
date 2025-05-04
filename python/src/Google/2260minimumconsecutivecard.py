"""
LeetCode 2260 - Minimum Consecutive Cards to Pick Up

Problem Statement:
You are given an integer array cards where cards[i] represents the value of the ith card.
A pair of cards are matching if the cards have the same value.
Return the minimum number of consecutive cards you have to pick up to have a pair of matching cards.
If it is impossible to have matching cards, return -1.

Time Complexity: O(n) where n is length of cards array
Space Complexity: O(n) for storing last seen positions
"""


class Solution:
    def minimumCardPickup(self, cards: list[int]) -> int:
        """
        Logic:
        1. Use hash map to store last seen position of each card
        2. For each card:
           - If card seen before, calculate distance to last occurrence
           - Update minimum distance if current distance is smaller
           - Update last seen position
        3. Return minimum distance found or -1 if no matches

        Args:
            cards: List of integers representing card values
        Returns:
            Minimum number of consecutive cards to pick up for a match
        """
        last_seen = {}
        min_distance = float('inf')

        for i, card in enumerate(cards):
            if card in last_seen:
                # Calculate the distance between two cards
                min_distance = min(min_distance, i - last_seen[card] + 1)
            # Update the last seen position of the card
            last_seen[card] = i

        return min_distance if min_distance != float('inf') else -1


# Test driver
def main():
    # Test cases
    test_cases = [
        {
            'cards': [3, 4, 2, 3, 4, 7],
            'expected': 4
        },
        {
            'cards': [1, 0, 5, 3],
            'expected': -1
        },
        {
            'cards': [1, 1],
            'expected': 2
        },
        {
            'cards': [95, 11, 8, 65, 5, 86, 30, 27, 30, 73, 15, 91, 30, 7, 37, 26, 55, 76, 60, 43, 36, 85, 47, 96, 6],
            'expected': 3
        }
    ]

    solution = Solution()

    for i, test in enumerate(test_cases, 1):
        result = solution.minimumCardPickup(test['cards'])
        status = "PASSED" if result == test['expected'] else "FAILED"
        print(f"Test {i}: {status}")
        print(f"Input: cards = {test['cards']}")
        print(f"Output: {result}")
        print(f"Expected: {test['expected']}\n")


if __name__ == "__main__":
    main()
