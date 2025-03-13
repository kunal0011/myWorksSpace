"""
LeetCode 754: Reach a Number

You are standing at position 0 on an infinite number line. You move with the following rules:
- On each move, you can either go left or right.
- During the nth move (starting from 1), you take n steps.

Given a target position target, return the minimum number of moves required to reach the target.

Note:
- target will be a non-zero integer in the range [-10^9, 10^9].
"""


class Solution:
    def reachNumber(self, target: int) -> int:
        """
        Optimized solution using mathematical properties
        Time complexity: O(sqrt(target))
        Space complexity: O(1)
        """
        target = abs(target)  # Problem is symmetric
        
        # Calculate minimum steps needed to reach or exceed target
        n = int((2 * target) ** 0.5)
        while (n * (n + 1)) // 2 < target:
            n += 1
            
        total = (n * (n + 1)) // 2
        
        # If difference is even, we can flip signs to reach exactly target
        if (total - target) % 2 == 0:
            return n
            
        # If difference is odd, we need 1 or 2 more steps
        return n + 1 + (n % 2)
    
    def reachNumber_bruteforce(self, target: int) -> int:
        """
        Alternative brute force solution for comparison
        Not recommended for large targets
        """
        target = abs(target)
        step = 0
        total = 0
        
        while total < target or (total - target) % 2 != 0:
            step += 1
            total += step
            
        return step


def test_reach_number():
    """Comprehensive test function for Reach a Number"""
    test_cases = [
        (3, 2),
        (2, 3),
        (4, 3),
        (-1000000000, 44721),
        (1, 1),
        (-1, 1),
        (5, 5),
        (0, 0),
        (100, 15),
        (-7, 4)
    ]
    
    solution = Solution()
    
    for i, (target, expected) in enumerate(test_cases, 1):
        # Test optimized solution
        result1 = solution.reachNumber(target)
        # Test brute force solution for small inputs
        result2 = solution.reachNumber_bruteforce(target) if abs(target) < 1000 else None
        
        print(f"\nTest case {i}:")
        print(f"Target: {target}")
        print(f"Expected: {expected}")
        print(f"Optimized: {result1} {'✓' if result1 == expected else '✗'}")
        if result2 is not None:
            print(f"Brute Force: {result2} {'✓' if result2 == expected else '✗'}")
        
        # Verify the solution is actually reachable
        if abs(target) < 1000:
            steps = result1
            total = (steps * (steps + 1)) // 2
            diff = total - abs(target)
            is_valid = diff >= 0 and diff % 2 == 0
            print(f"Solution valid: {'✓' if is_valid else '✗'}")


if __name__ == "__main__":
    test_reach_number()
