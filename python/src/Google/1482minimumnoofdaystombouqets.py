from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # Helper function to determine if we can make m bouquets in 'days'
        def canMakeBouquets(days: int) -> bool:
            bouquets = 0
            flowers = 0
            for bloom in bloomDay:
                if bloom <= days:
                    flowers += 1
                    # If we have enough flowers for a bouquet
                    if flowers == k:
                        bouquets += 1
                        flowers = 0  # Reset the flower counter for the next bouquet
                else:
                    flowers = 0  # Reset if a flower hasn't bloomed

                if bouquets >= m:
                    return True

            return bouquets >= m

        # Edge case: if there are not enough flowers to make m bouquets
        if len(bloomDay) < m * k:
            return -1

        # Binary search for the minimum day
        left, right = min(bloomDay), max(bloomDay)

        while left < right:
            mid = (left + right) // 2
            if canMakeBouquets(mid):
                right = mid  # Try for fewer days
            else:
                left = mid + 1  # Increase the days

        return left if canMakeBouquets(left) else -1
