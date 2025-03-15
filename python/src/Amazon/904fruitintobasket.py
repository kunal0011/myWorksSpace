"""
LeetCode 904: Fruit Into Baskets

You are visiting a farm that has a single row of fruit trees arranged from left to right.
The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:
- You only have two baskets, and each basket can only hold a single type of fruit. 
- Starting from any tree, you must pick exactly one fruit from every tree while moving to the right.
- Once you reach a tree with fruit that cannot fit in your baskets, you must stop.

Return the maximum number of fruits you can collect using these rules.

Constraints:
- 1 <= fruits.length <= 10^5
- 0 <= fruits[i] < fruits.length
"""

from typing import List
from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = defaultdict(int)  # type -> count
        max_fruits = 0
        start = 0
        
        for end, fruit in enumerate(fruits):
            basket[fruit] += 1
            
            # If we have more than 2 types, shrink window
            while len(basket) > 2:
                basket[fruits[start]] -= 1
                if basket[fruits[start]] == 0:
                    del basket[fruits[start]]
                start += 1
                
            max_fruits = max(max_fruits, end - start + 1)
            
        return max_fruits

def validate_fruits(fruits: List[int]) -> bool:
    """Validate input according to constraints"""
    if not 1 <= len(fruits) <= 10**5:
        return False
    return all(0 <= x < len(fruits) for x in fruits)

def test_total_fruit():
    """Test function for Fruit Into Baskets"""
    test_cases = [
        ([1,2,1], 3),
        ([0,1,2,2], 3),
        ([1,2,3,2,2], 4),
        ([3,3,3,1,2,1,1,2,3,3,4], 5),
        ([1,1,1,1,2,2,3,3,3], 5),
        ([0], 1),
        ([1,2,1,2,1,2,1,2], 8)
    ]
    
    solution = Solution()
    
    for i, (fruits, expected) in enumerate(test_cases, 1):
        is_valid = validate_fruits(fruits)
        result = solution.totalFruit(fruits)
        
        print(f"\nTest case {i}:")
        print("Fruit trees:", fruits)
        
        # Visualize the fruits
        tree_line = ""
        for fruit in fruits:
            tree_line += f"🌳{fruit} "
        print("Trees:", tree_line)
        
        # Show the maximum subarray
        if result > 0:
            found = False
            start = 0
            basket = defaultdict(int)
            for end, fruit in enumerate(fruits):
                basket[fruit] += 1
                while len(basket) > 2:
                    basket[fruits[start]] -= 1
                    if basket[fruits[start]] == 0:
                        del basket[fruits[start]]
                    start += 1
                if end - start + 1 == result:
                    print("Best sequence:", fruits[start:end+1])
                    print(f"Using baskets: {list(basket.keys())}")
                    found = True
                    break
                    
        print(f"Maximum fruits: {result}")
        print(f"Expected: {expected}")
        print(f"Valid input: {'✓' if is_valid else '✗'}")
        print(f"Test passed: {'✓' if result == expected else '✗'}")
        
        # Additional statistics
        unique_fruits = len(set(fruits))
        print(f"Total trees: {len(fruits)}")
        print(f"Unique fruit types: {unique_fruits}")
        print(f"Collection efficiency: {result/len(fruits)*100:.1f}%")

if __name__ == "__main__":
    test_total_fruit()
