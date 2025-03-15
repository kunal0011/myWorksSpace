"""
LeetCode 997: Find the Town Judge

In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

The town judge:
1. Trusts nobody
2. Everybody (except for the town judge) trusts the town judge
3. There is exactly one person that satisfies properties 1 and 2

You are given an array trust where trust[i] = [ai, bi] represents that person ai trusts person bi.
Return the label of the town judge if they exist, and return -1 otherwise.

Constraints:
- 1 <= n <= 1000
- 0 <= trust.length <= 10^4
- trust[i].length == 2
- All pairs trust[i] are unique
- ai != bi
- 1 <= ai, bi <= n
"""

from typing import List
from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and not trust:
            return 1
            
        # Track both incoming and outgoing trust
        trusted = [0] * (n + 1)  # Count of people who trust each person
        trusts = [0] * (n + 1)   # Count of people each person trusts
        
        for a, b in trust:
            trusted[b] += 1  # b is trusted by a
            trusts[a] += 1   # a trusts someone
            
        # Find person trusted by all others but trusts no one
        for i in range(1, n + 1):
            if trusted[i] == n - 1 and trusts[i] == 0:
                return i
                
        return -1

def validate_input(n: int, trust: List[List[int]]) -> bool:
    """Validate input according to constraints"""
    if not 1 <= n <= 1000:
        return False
    if not 0 <= len(trust) <= 10**4:
        return False
    
    seen = set()
    for a, b in trust:
        if not (1 <= a <= n and 1 <= b <= n):
            return False
        if a == b:
            return False
        if (a, b) in seen:
            return False
        seen.add((a, b))
    return True

def visualize_trust(n: int, trust: List[List[int]]) -> None:
    """Create visual representation of trust relationships"""
    # Create adjacency matrix
    matrix = [[' ' for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n+1):
        matrix[i][0] = str(i)
        matrix[0][i] = str(i)
    
    # Fill trust relationships
    for a, b in trust:
        matrix[a][b] = '✓'
        
    # Print matrix
    print("\nTrust relationships (✓ means row trusts column):")
    for row in matrix:
        print(' '.join(f"{x:2}" for x in row))

def test_find_judge():
    """Test function for Find the Town Judge"""
    test_cases = [
        (2, [[1,2]], 2),
        (3, [[1,3],[2,3]], 3),
        (3, [[1,3],[2,3],[3,1]], -1),
        (3, [[1,2],[2,3]], -1),
        (4, [[1,3],[1,4],[2,3],[2,4],[4,3]], 3),
        (1, [], 1)
    ]
    
    solution = Solution()
    
    for i, (n, trust, expected) in enumerate(test_cases, 1):
        is_valid = validate_input(n, trust)
        result = solution.findJudge(n, trust)
        
        print(f"\nTest case {i}:")
        print(f"Number of people: {n}")
        print(f"Trust relationships: {trust}")
        
        visualize_trust(n, trust)
        
        print(f"\nExpected judge: {expected}")
        print(f"Found judge: {result}")
        print(f"Valid input: {'✓' if is_valid else '✗'}")
        print(f"Test passed: {'✓' if result == expected else '✗'}")
        
        if result != -1:
            # Show evidence for judge
            trusted_by = sum(1 for a, b in trust if b == result)
            trusts_others = sum(1 for a, b in trust if a == result)
            print(f"\nEvidence for person {result}:")
            print(f"Trusted by {trusted_by} people")
            print(f"Trusts {trusts_others} people")
            print(f"Valid judge: {'✓' if trusted_by == n-1 and trusts_others == 0 else '✗'}")

if __name__ == "__main__":
    test_find_judge()
