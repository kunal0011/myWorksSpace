from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Helper function to convert time "HH:MM" to total minutes
        def timeToMinutes(time: str) -> int:
            hours, minutes = map(int, time.split(":"))
            return hours * 60 + minutes

        # Convert all time points to minutes
        minutes = [timeToMinutes(time) for time in timePoints]

        # Sort the time points
        minutes.sort()

        # Initialize the minimum difference to a large value
        min_diff = float('inf')

        # Calculate the difference between consecutive time points
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i - 1])

        # Compare the circular difference between the first and last time point
        min_diff = min(min_diff, 1440 - (minutes[-1] - minutes[0]))

        return min_diff


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    timePoints = ["23:59", "00:00"]
    print(sol.findMinDifference(timePoints))  # Expected output: 1

    # Test case 2
    timePoints = ["12:01", "23:59", "00:00"]
    print(sol.findMinDifference(timePoints))  # Expected output: 1
