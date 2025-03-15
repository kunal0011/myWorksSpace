"""
LeetCode 849: Maximize Distance to Closest Person

You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, 
and seats[i] = 0 represents that the ith seat is empty.

There is at least one empty seat, and at least one person sitting.
Return the maximum distance to the closest person.

Constraints:
- 2 <= seats.length <= 2 * 10^4
- seats[i] is 0 or 1
- At least one seat is empty
- At least one seat is occupied
"""

from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        prev_person = None
        max_dist = 0
        
        # One pass solution
        for i in range(n):
            if seats[i] == 1:
                # If this is first person, check distance to start
                if prev_person is None:
                    max_dist = i
                else:
                    # Check distance between two people
                    max_dist = max(max_dist, (i - prev_person) // 2)
                prev_person = i
        
        # Check distance from last person to end
        if prev_person is not None:
            max_dist = max(max_dist, n - 1 - prev_person)
            
        return max_dist

def validate_seats(seats: List[int]) -> bool:
    """Validate seats array according to constraints"""
    if not 2 <= len(seats) <= 2 * 10**4:
        return False
    if not all(seat in (0, 1) for seat in seats):
        return False
    if 1 not in seats or 0 not in seats:
        return False
    return True

def visualize_seats(seats: List[int], chosen_pos: int = -1) -> str:
    """Create a visual representation of seats"""
    result = ""
    for i, seat in enumerate(seats):
        if i == chosen_pos:
            result += "X"  # Position to sit
        elif seat == 1:
            result += "P"  # Person
        else:
            result += "_"  # Empty seat
    return result

def test_max_distance():
    """Test function for Max Distance to Closest Person"""
    test_cases = [
        ([1,0,0,0,1,0,1], 2),
        ([1,0,0,0], 3),
        ([0,1], 1),
        ([1,0,0,0,0,1,0,0], 2),
        ([0,0,1,0,0,0,1,0], 2),
        ([0,0,0,1,0,0,0,1,0,0], 3)
    ]
    
    solution = Solution()
    
    for i, (seats, expected) in enumerate(test_cases, 1):
        is_valid = validate_seats(seats)
        result = solution.maxDistToClosest(seats)
        
        print(f"\nTest case {i}:")
        print(f"Seats arrangement: {seats}")
        
        # Find optimal position
        optimal_pos = -1
        if result > 0:
            for j in range(len(seats)):
                if seats[j] == 0:  # Empty seat
                    dist = float('inf')
                    for k in range(len(seats)):
                        if seats[k] == 1:
                            dist = min(dist, abs(j - k))
                    if dist == result:
                        optimal_pos = j
                        break
                        
        print("Visualization:")
        print(visualize_seats(seats, optimal_pos))
        print(f"Maximum distance: {result}")
        print(f"Expected distance: {expected}")
        print(f"Valid input: {'✓' if is_valid else '✗'}")
        print(f"Test passed: {'✓' if result == expected else '✗'}")
        
        # Additional statistics
        occupied = sum(seats)
        print(f"Total seats: {len(seats)}")
        print(f"Occupied seats: {occupied}")
        print(f"Empty seats: {len(seats) - occupied}")

if __name__ == "__main__":
    test_max_distance()
