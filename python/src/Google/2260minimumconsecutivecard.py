class Solution:
    def minimumCardPickup(self, cards: list[int]) -> int:
        last_seen = {}
        min_distance = float('inf')

        for i, card in enumerate(cards):
            if card in last_seen:
                # Calculate the distance between two cards
                min_distance = min(min_distance, i - last_seen[card] + 1)
            # Update the last seen position of the card
            last_seen[card] = i

        return min_distance if min_distance != float('inf') else -1
