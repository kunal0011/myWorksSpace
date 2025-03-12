"""
LeetCode 539 - Minimum Time Difference

Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference 
between any two time points in the list.

Example 1:
Input: timePoints = ["23:59","00:00"]
Output: 1
Explanation: The minimum difference is 1 minute between 23:59 and 00:00.

Example 2:
Input: timePoints = ["00:00","23:59","00:00"]
Output: 0
Explanation: The minimum difference is 0 minutes between 00:00 and 00:00.

Constraints:
- 2 <= timePoints.length <= 2 * 104
- timePoints[i] is in the format "HH:MM"
"""

from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        """
        Optimized solution using sorting.
        Time complexity: O(n log n)
        Space complexity: O(n)
        """
        # Convert all times to minutes since midnight
        minutes = sorted(self._convert_to_minutes(t) for t in timePoints)
        
        if len(minutes) != len(set(minutes)):
            return 0  # If there are duplicates, minimum difference is 0
            
        min_diff = float('inf')
        
        # Compare adjacent times
        for i in range(len(minutes)):
            curr_diff = minutes[(i + 1) % len(minutes)] - minutes[i]
            if i == len(minutes) - 1:  # Handle wrap-around case
                curr_diff = curr_diff % 1440  # 24 * 60 = 1440 minutes in a day
            min_diff = min(min_diff, curr_diff)
            
        # Check wrap-around case between first and last time
        wrap_diff = (1440 - minutes[-1]) + minutes[0]
        return min(min_diff, wrap_diff)
    
    def _convert_to_minutes(self, time: str) -> int:
        """Helper function to convert time string to minutes since midnight"""
        hours, minutes = map(int, time.split(':'))
        return hours * 60 + minutes

    def findMinDifference_bucket(self, timePoints: List[str]) -> int:
        """
        Alternative solution using bucket sort approach.
        Time complexity: O(n)
        Space complexity: O(1) since we have fixed 1440 minutes
        """
        # Use boolean array to mark if minute exists
        minutes_seen = [False] * 1440
        
        for time in timePoints:
            minutes = self._convert_to_minutes(time)
            if minutes_seen[minutes]:  # If we've seen this time before
                return 0
            minutes_seen[minutes] = True
        
        # Find first and last true values
        first = next(i for i in range(1440) if minutes_seen[i])
        last = next(i for i in range(1439, -1, -1) if minutes_seen[i])
        
        min_diff = float('inf')
        prev = first
        
        # Find minimum difference between consecutive times
        for curr in range(first + 1, 1440):
            if minutes_seen[curr]:
                min_diff = min(min_diff, curr - prev)
                prev = curr
        
        # Consider wrap-around case
        return min(min_diff, (1440 - last + first))


def test_minimum_time_difference():
    """Test function to verify both solution approaches"""
    solution = Solution()
    
    test_cases = [
        # Basic test cases from problem description
        (["23:59","00:00"], 1),
        (["00:00","23:59","00:00"], 0),
        
        # Additional test cases
        (["00:00","00:01"], 1),
        (["12:00","12:01"], 1),
        (["01:01","02:01"], 60),
        (["00:00","04:00","22:00"], 120),
        (["00:00","23:58","23:59"], 1),
        (["12:12","12:13","12:14"], 1),
        (["00:00","00:15","00:30","01:00","12:00"], 15),
        (["23:59","00:00","00:01"], 1),
        (["00:00","14:30","23:59"], 1),
        (["01:39","10:26","21:43"], 529)
    ]
    
    for i, (timePoints, expected) in enumerate(test_cases, 1):
        # Test sorting-based solution
        result_sort = solution.findMinDifference(timePoints)
        # Test bucket-based solution
        result_bucket = solution.findMinDifference_bucket(timePoints)
        
        status_sort = "✓" if result_sort == expected else "✗"
        status_bucket = "✓" if result_bucket == expected else "✗"
        
        print(f"\nTest {i}:")
        print(f"Input: timePoints = {timePoints}")
        print(f"Sorting Solution: {status_sort} Got: {result_sort}")
        print(f"Bucket Solution: {status_bucket} Got: {result_bucket}")
        print(f"Expected: {expected}")
        
        # Additional verification for failed cases
        if status_sort == "✗":
            print(f"Sorting solution failed! Expected {expected}, got {result_sort}")
        if status_bucket == "✗":
            print(f"Bucket solution failed! Expected {expected}, got {result_bucket}")


if __name__ == "__main__":
    test_minimum_time_difference()