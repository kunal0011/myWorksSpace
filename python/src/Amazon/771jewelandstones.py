"""
LeetCode 771: Jewels and Stones

You're given strings jewels representing the types of stones that are jewels, 
and stones representing the stones you have. Each character in stones is a type 
of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

Constraints:
- 1 <= jewels.length, stones.length <= 50
- jewels and stones consist of only English letters
- All characters in jewels are unique
"""


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        """
        Optimized solution using set for O(1) lookups
        Time complexity: O(J + S) where J = len(jewels), S = len(stones)
        Space complexity: O(J)
        """
        jewel_set = set(jewels)
        return sum(stone in jewel_set for stone in stones)
    
    def numJewelsInStones_dict(self, jewels: str, stones: str) -> int:
        """
        Alternative solution using dictionary for stone counting
        Time complexity: O(J + S)
        Space complexity: O(S)
        """
        from collections import Counter
        stone_count = Counter(stones)
        return sum(stone_count[j] for j in jewels)
    
    def numJewelsInStones_oneliner(self, jewels: str, stones: str) -> int:
        """
        One-liner solution, less efficient but more concise
        """
        return len([s for s in stones if s in jewels])


def validate_jewels_count(jewels: str, stones: str, count: int) -> bool:
    """Validate the jewel count is correct"""
    # Check constraints
    if not (1 <= len(jewels) <= 50 and 1 <= len(stones) <= 50):
        return False
    # Check if jewels are unique
    if len(jewels) != len(set(jewels)):
        return False
    # Verify the count manually
    manual_count = sum(stone in set(jewels) for stone in stones)
    return manual_count == count


def test_jewels_and_stones():
    """Test function for Jewels and Stones solutions"""
    test_cases = [
        ("aA", "aAAbbbb", 3),
        ("z", "ZZ", 0),
        ("ABC", "ABCDEF", 3),
        ("aAbB", "aAbBcCdD", 4),
        ("", "ABC", 0),  # Edge case
        ("a", "a", 1),
        ("ABCD", "abcd", 0),  # Case sensitivity test
    ]
    
    solution = Solution()
    
    for i, (jewels, stones, expected) in enumerate(test_cases, 1):
        print(f"\nTest case {i}:")
        print(f"Jewels: {jewels}")
        print(f"Stones: {stones}")
        print(f"Expected: {expected}")
        
        # Test all three implementations
        result1 = solution.numJewelsInStones(jewels, stones)
        result2 = solution.numJewelsInStones_dict(jewels, stones)
        result3 = solution.numJewelsInStones_oneliner(jewels, stones)
        
        print(f"Set solution: {result1} {'✓' if result1 == expected else '✗'}")
        print(f"Dict solution: {result2} {'✓' if result2 == expected else '✗'}")
        print(f"One-liner: {result3} {'✓' if result3 == expected else '✗'}")
        
        # Validate the result
        is_valid = validate_jewels_count(jewels, stones, result1)
        print(f"Valid solution: {'✓' if is_valid else '✗'}")


if __name__ == "__main__":
    test_jewels_and_stones()
