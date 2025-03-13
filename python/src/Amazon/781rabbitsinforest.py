"""
LeetCode 781: Rabbits in Forest

There is a forest with an unknown number of rabbits. We asked n rabbits "How many rabbits 
have the same color as you?" and collected the answers in an array 'answers' where:
- answers[i] is the answer from the i-th rabbit

Given the array 'answers', return the minimum number of rabbits that could be in the forest.

Constraints:
- 1 <= answers.length <= 1000
- 0 <= answers[i] < 1000
"""

from collections import Counter
from typing import List
from math import ceil


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        """
        Optimized solution using math.ceil for group calculations
        Time complexity: O(n)
        Space complexity: O(k) where k is unique answers
        """
        if not answers:
            return 0
            
        count = Counter(answers)
        total = 0
        
        for same_color, rabbits_seen in count.items():
            group_size = same_color + 1  # Each group has answer+1 rabbits
            # Calculate minimum groups needed using ceil
            groups = ceil(rabbits_seen / group_size)
            total += groups * group_size
            
        return total
    
    def numRabbits_alternative(self, answers: List[int]) -> int:
        """
        Alternative solution without using ceil
        Time complexity: O(n)
        Space complexity: O(k)
        """
        count = Counter(answers)
        return sum(((num + ans) // (ans + 1)) * (ans + 1) 
                  for ans, num in count.items())


def validate_rabbits(answers: List[int], result: int) -> bool:
    """
    Validate if the result is possible given the answers
    """
    if not answers and result == 0:
        return True
        
    if result < len(answers):
        return False
        
    # Check if result satisfies minimum rabbits needed
    count = Counter(answers)
    for same_color, rabbits_seen in count.items():
        if rabbits_seen > same_color + 1:  # More rabbits than possible in one group
            min_groups = (rabbits_seen + same_color) // (same_color + 1)
            min_rabbits = min_groups * (same_color + 1)
            if result < min_rabbits:
                return False
                
    return True


def test_rabbits_in_forest():
    """Test function for Rabbits in Forest solutions"""
    test_cases = [
        ([1, 1, 2], 5),
        ([10, 10, 10], 11),
        ([], 0),
        ([1], 2),
        ([0, 0, 1, 1, 1], 6),
        ([2, 2, 2, 2, 2, 2], 6),
        ([1, 0, 1, 0, 0], 5),
        ([1, 1, 1, 1, 1], 6)
    ]
    
    solution = Solution()
    
    for i, (answers, expected) in enumerate(test_cases, 1):
        # Test both implementations
        result1 = solution.numRabbits(answers)
        result2 = solution.numRabbits_alternative(answers)
        
        print(f"\nTest case {i}:")
        print(f"Answers: {answers}")
        print(f"Expected minimum rabbits: {expected}")
        print(f"Optimized solution: {result1} {'✓' if result1 == expected else '✗'}")
        print(f"Alternative solution: {result2} {'✓' if result2 == expected else '✗'}")
        
        # Validate the solution
        is_valid = validate_rabbits(answers, result1)
        print(f"Valid solution: {'✓' if is_valid else '✗'}")


if __name__ == "__main__":
    test_rabbits_in_forest()
