"""
LeetCode 735: Asteroid Collision

We are given an array asteroids of integers representing asteroids in a row.
For each asteroid, the absolute value represents its size, and the sign represents 
its direction (positive = right, negative = left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the 
smaller one will explode. If both are the same size, both will explode. Two asteroids 
moving in the same direction will never meet.
"""

from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if not asteroids:
            return []
            
        stack = []
        
        for asteroid in asteroids:
            # Only process collisions when current asteroid is moving left (-ve)
            # and there are asteroids moving right (+ve) in the stack
            while stack and asteroid < 0 < stack[-1]:
                # If top asteroid is smaller, it gets destroyed, continue checking
                if stack[-1] < -asteroid:
                    stack.pop()
                    continue
                # If equal size, both get destroyed
                elif stack[-1] == -asteroid:
                    stack.pop()
                    break
                # If current asteroid is smaller, it gets destroyed
                else:
                    break
            # Add asteroid to stack if:
            # 1. Stack is empty, or
            # 2. No collision occurred (while loop didn't break), or
            # 3. Both asteroids were destroyed (stack.pop() in elif)
            else:
                stack.append(asteroid)
                
        return stack


def test_asteroid_collision():
    """Test function for asteroidCollision with multiple test cases"""
    test_cases = [
        ([5,10,-5], [5,10]),                    # Basic collision
        ([8,-8], []),                           # Equal size collision
        ([10,2,-5], [10]),                      # Multiple collisions
        ([-2,-1,1,2], [-2,-1,1,2]),            # No collisions
        ([1,-1,-2,-3], [-2,-3]),               # Sequential collisions
        ([1,2,3,-3], [1,2]),                   # Right-moving survivors
        ([-5,5], [-5,5]),                      # Moving away from each other
        ([], []),                              # Empty input
        ([1], [1]),                            # Single asteroid
        ([-1], [-1])                           # Single asteroid moving left
    ]
    
    solution = Solution()
    for i, (asteroids, expected) in enumerate(test_cases, 1):
        result = solution.asteroidCollision(asteroids)
        success = result == expected
        print(f"\nTest case {i}:")
        print(f"Input: {asteroids}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"{'✓ Passed' if success else '✗ Failed'}")


if __name__ == "__main__":
    test_asteroid_collision()
