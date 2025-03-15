"""
LeetCode 970: Powerful Integers

Given three integers x, y, and bound, return a list of all the powerful integers that have 
a value less than or equal to bound.

An integer is powerful if it can be represented as x^i + y^j for some integers i >= 0 and j >= 0.

You may return the answer in any order. Make sure each value is included in the answer only once.

Constraints:
- 1 <= x, y <= 100
- 0 <= bound <= 10^6
"""

from typing import List
from math import log

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if bound < 2:  # Early return for small bound
            return []
            
        # Calculate maximum possible exponents
        i_max = int(log(bound, x)) + 1 if x > 1 else 1
        j_max = int(log(bound, y)) + 1 if y > 1 else 1
        
        powerful = set()
        
        for i in range(i_max):
            x_power = x ** i
            if x_power > bound:
                break
                
            for j in range(j_max):
                val = x_power + y ** j
                if val > bound:
                    break
                powerful.add(val)
                if y == 1:
                    break
            if x == 1:
                break
                
        return sorted(powerful)  # Return sorted for consistency

def validate_input(x: int, y: int, bound: int) -> bool:
    """Validate input according to constraints"""
    if not (1 <= x <= 100 and 1 <= y <= 100):
        return False
    if not 0 <= bound <= 10**6:
        return False
    return True

def test_powerful_integers():
    """Test function for Powerful Integers"""
    test_cases = [
        (2, 3, 10, [2, 3, 4, 5, 7, 9, 10]),
        (3, 5, 15, [2, 4, 6, 8, 10, 14]),
        (2, 1, 10, [2, 3, 5, 9]),
        (1, 1, 10, [2]),
        (2, 2, 20, [2, 3, 5, 9, 17]),
        (5, 3, 50, [2, 4, 6, 8, 10, 14, 26, 28, 34, 46])
    ]
    
    solution = Solution()
    
    for i, (x, y, bound, expected) in enumerate(test_cases, 1):
        is_valid = validate_input(x, y, bound)
        result = solution.powerfulIntegers(x, y, bound)
        
        print(f"\nTest case {i}:")
        print(f"x = {x}, y = {y}, bound = {bound}")
        
        # Show calculations
        print("\nPower combinations:")
        for i_val in range(5):  # Show first few combinations
            for j_val in range(5):
                val = x**i_val + y**j_val
                if val <= bound:
                    print(f"{x}^{i_val} + {y}^{j_val} = {val}")
        
        print(f"\nResult: {result}")
        print(f"Expected: {expected}")
        print(f"Valid input: {'✓' if is_valid else '✗'}")
        print(f"Test passed: {'✓' if result == expected else '✗'}")
        
        # Additional statistics
        print("\nStatistics:")
        print(f"Number of powerful integers: {len(result)}")
        if result:
            print(f"Range: [{min(result)}, {max(result)}]")
            print(f"Average value: {sum(result)/len(result):.2f}")

if __name__ == "__main__":
    test_powerful_integers()
