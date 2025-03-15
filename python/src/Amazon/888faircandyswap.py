"""
LeetCode 888: Fair Candy Swap

Alice and Bob have candy bars of different sizes. Each array represents the size of candy bars they have.
Alice and Bob want to exchange exactly one candy bar each so that they both end up with the same total candy.
Return [x, y] where x is the size of the candy bar that Alice must exchange, and y is the size of the candy bar that Bob must exchange.

Constraints:
- 1 <= AliceSizes.length, BobSizes.length <= 10^4
- 1 <= AliceSizes[i], BobSizes[j] <= 10^5
- At least one answer exists
"""

from typing import List

class Solution:
    def fairCandySwap(self, AliceSizes: List[int], BobSizes: List[int]) -> List[int]:
        sum_alice = sum(AliceSizes)
        sum_bob = sum(BobSizes)
        delta = (sum_alice - sum_bob) // 2
        
        # Use set for O(1) lookup
        bob_set = set(BobSizes)
        
        # For each candy x in Alice's collection
        # Find y in Bob's collection where y = x - delta
        for x in AliceSizes:
            target = x - delta
            if target in bob_set:
                return [x, target]
        
        return []  # Should never reach here given problem constraints

def validate_input(AliceSizes: List[int], BobSizes: List[int]) -> bool:
    """Validate input according to constraints"""
    if not (1 <= len(AliceSizes) <= 10**4 and 1 <= len(BobSizes) <= 10**4):
        return False
    if not all(1 <= x <= 10**5 for x in AliceSizes + BobSizes):
        return False
    return True

def test_fair_candy_swap():
    """Test function for Fair Candy Swap"""
    test_cases = [
        ([1,1], [2,2], [1,2]),
        ([1,2], [2,3], [2,3]),
        ([2], [1,3], [2,3]),
        ([1,2,5], [2,4], [5,4]),
        ([35,17,4,24,10], [63,21], [24,21])
    ]
    
    solution = Solution()
    
    for i, (alice, bob, expected) in enumerate(test_cases, 1):
        is_valid = validate_input(alice, bob)
        result = solution.fairCandySwap(alice, bob)
        
        # Calculate totals before and after swap
        initial_alice = sum(alice)
        initial_bob = sum(bob)
        
        if result:
            final_alice = initial_alice - result[0] + result[1]
            final_bob = initial_bob - result[1] + result[0]
        else:
            final_alice = final_bob = 0
            
        print(f"\nTest case {i}:")
        print(f"Alice's candies: {alice} (sum: {initial_alice})")
        print(f"Bob's candies: {bob} (sum: {initial_bob})")
        print(f"Expected swap: {expected}")
        print(f"Actual swap: {result}")
        print(f"Valid input: {'✓' if is_valid else '✗'}")
        print(f"Test passed: {'✓' if result == expected else '✗'}")
        if result:
            print(f"After swap - Alice: {final_alice}, Bob: {final_bob}")
            print(f"Fair distribution: {'✓' if final_alice == final_bob else '✗'}")

if __name__ == "__main__":
    test_fair_candy_swap()
