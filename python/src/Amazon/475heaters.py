import bisect


class Solution:
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        # Sort both the houses and heaters arrays
        houses.sort()
        heaters.sort()
        max_radius = 0

        # For each house, find the minimum distance to a heater
        for house in houses:
            # Find the closest heater to the left or right using binary search
            idx = bisect.bisect_left(heaters, house)

            # Calculate distances to the closest heaters on both sides (if they exist)
            dist_left = float('inf') if idx == 0 else house - heaters[idx - 1]
            dist_right = float('inf') if idx == len(
                heaters) else heaters[idx] - house

            # Take the smaller of the two distances
            min_dist = min(dist_left, dist_right)

            # Track the maximum of the minimum distances (the required radius)
            max_radius = max(max_radius, min_dist)

        return max_radius


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    houses1 = [1, 2, 3]
    heaters1 = [2]
    print(sol.findRadius(houses1, heaters1))  # Expected output: 1

    # Test case 2
    houses2 = [1, 2, 3, 4]
    heaters2 = [1, 4]
    print(sol.findRadius(houses2, heaters2))  # Expected output: 1

    # Test case 3
    houses3 = [1, 5]
    heaters3 = [2]
    print(sol.findRadius(houses3, heaters3))  # Expected output: 3
