"""
LeetCode 881: Boats to Save People

You are given an array people where people[i] is the weight of the ith person, 
and an infinite number of boats where each boat can carry a maximum weight of limit. 
Each boat carries at most two people at the same time.

Return the minimum number of boats to carry every given person.

Constraints:
- 1 <= people.length <= 5 * 10^4
- 1 <= people[i] <= limit <= 3 * 10^4
"""

from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Early return for single person
        if len(people) == 1:
            return 1
            
        people.sort()  # Sort by weight
        boats = 0
        left, right = 0, len(people) - 1
        
        while left <= right:
            # Try to pair heaviest person with lightest
            if left == right:
                boats += 1
                break
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            boats += 1
            
        return boats

def validate_input(people: List[int], limit: int) -> bool:
    """Validate input according to constraints"""
    if not 1 <= len(people) <= 5 * 10**4:
        return False
    if not all(1 <= x <= limit <= 3 * 10**4 for x in people):
        return False
    return True

def test_rescue_boats():
    """Test function for Boats to Save People"""
    test_cases = [
        ([1,2], 3, 1),
        ([3,2,2,1], 3, 3),
        ([3,5,3,4], 5, 4),
        ([1,2,3,4], 5, 2),
        ([4,4,4,4], 4, 4),
        ([1,1,1,2,2,2], 3, 3),
        ([2,2], 6, 1),
        ([1,2,3,4,5], 6, 3)
    ]
    
    solution = Solution()
    
    for i, (people, limit, expected) in enumerate(test_cases, 1):
        # Make a copy to preserve original array
        people_copy = people.copy()
        is_valid = validate_input(people_copy, limit)
        result = solution.numRescueBoats(people_copy, limit)
        
        print(f"\nTest case {i}:")
        print(f"People weights: {people}")
        print(f"Weight limit: {limit}")
        print(f"Expected boats: {expected}")
        print(f"Actual boats: {result}")
        print(f"Valid input: {'✓' if is_valid else '✗'}")
        print(f"Test passed: {'✓' if result == expected else '✗'}")
        
        # Additional statistics
        print(f"Total people: {len(people)}")
        print(f"Weight range: {min(people)} to {max(people)}")
        print(f"Average people per boat: {len(people)/result:.2f}")
        print(f"Total weight: {sum(people)}")
        print(f"Average weight per boat: {sum(people)/result:.2f}")

if __name__ == "__main__":
    test_rescue_boats()
