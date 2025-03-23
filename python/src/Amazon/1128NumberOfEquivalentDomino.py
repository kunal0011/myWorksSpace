"""
LeetCode 1128: Number of Equivalent Domino Pairs

Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if 
either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

Constraints:
- 1 <= dominoes.length <= 4 * 10^4
- dominoes[i].length == 2
- 1 <= dominoes[i][j] <= 9
"""

from typing import List
from collections import defaultdict

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        pairs = defaultdict(int)
        count = 0
        
        # For each domino, store the canonical form (min,max)
        for a, b in dominoes:
            key = (min(a, b), max(a, b))
            # Each new domino can form a pair with all previous equivalent dominoes
            count += pairs[key]
            pairs[key] += 1
            
        return count

def validate_dominoes(dominoes: List[List[int]]) -> bool:
    """Validate input according to constraints"""
    if not 1 <= len(dominoes) <= 4 * 10**4:
        return False
    return all(len(d) == 2 and 1 <= d[0] <= 9 and 1 <= d[1] <= 9 for d in dominoes)

def find_equivalent_pairs(dominoes: List[List[int]]) -> List[tuple]:
    """Find all equivalent pairs for visualization (use only for small inputs)"""
    pairs = []
    for i in range(len(dominoes)):
        for j in range(i + 1, len(dominoes)):
            a, b = dominoes[i]
            c, d = dominoes[j]
            if (a == c and b == d) or (a == d and b == c):
                pairs.append((i, j))
    return pairs

def test_domino_pairs():
    """Test function for Number of Equivalent Domino Pairs"""
    test_cases = [
        ([[1,2],[2,1],[3,4],[5,6]], 1),
        ([[1,2],[1,2],[1,1],[1,2],[2,2]], 3),
        ([[1,1],[2,2],[1,1]], 1),
        ([[1,2],[2,1],[1,2]], 3),
        ([[1,1],[1,1],[1,1],[1,1]], 6)
    ]
    
    solution = Solution()
    
    for i, (dominoes, expected) in enumerate(test_cases, 1):
        is_valid = validate_dominoes(dominoes)
        result = solution.numEquivDominoPairs(dominoes)
        
        print(f"\nTest case {i}:")
        print("Dominoes:", dominoes)
        
        # For small inputs, show equivalent pairs
        if len(dominoes) <= 10:
            pairs = find_equivalent_pairs(dominoes)
            print("\nEquivalent pairs:")
            for pair in pairs:
                i, j = pair
                print(f"Domino {i}: {dominoes[i]} ≡ Domino {j}: {dominoes[j]}")
        
        print(f"\nExpected pairs: {expected}")
        print(f"Found pairs: {result}")
        print(f"Valid input: {'✓' if is_valid else '✗'}")
        print(f"Test passed: {'✓' if result == expected else '✗'}")
        
        # Additional statistics
        unique_values = set()
        for a, b in dominoes:
            unique_values.add(min(a, b))
            unique_values.add(max(a, b))
        print(f"\nStatistics:")
        print(f"Total dominoes: {len(dominoes)}")
        print(f"Unique values: {sorted(unique_values)}")
        print(f"Theoretical max pairs: {(len(dominoes) * (len(dominoes) - 1)) // 2}")

if __name__ == "__main__":
    test_domino_pairs()
