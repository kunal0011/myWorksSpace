"""
LeetCode 756: Pyramid Transition Matrix

Problem Statement:
You are given a bottom string and a list of allowed triples. Each triple is represented as a string of length 3.
You need to build a pyramid using these allowed triples where:
- The bottom row is the given bottom string
- For every two adjacent blocks in a row, you can place a block above them if the triple (bottom-left, bottom-right, top) is in allowed
Return true if you can build the pyramid all the way to the top (a single block), otherwise return false.

Logic:
1. Create a mapping from pairs of blocks to possible top blocks using allowed triples
2. Use backtracking to try all possible combinations for each level:
   - Base case: If row length is 1, we've reached the top (return True)
   - For each adjacent pair in current row:
     * Find all possible blocks that can go above them
     * Try each possibility recursively
   - If any combination works, return True
   - If no combination works, return False
3. Time Complexity: O(A^N) where A is average number of allowed blocks per pair, N is length of bottom
4. Space Complexity: O(N) for recursion stack
"""

from collections import defaultdict
from typing import List


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        # Step 1: Create a mapping from pairs to possible top blocks
        allowed_map = defaultdict(list)
        for triple in allowed:
            allowed_map[triple[:2]].append(triple[2])

        # Step 2: Recursive function to check if we can build the pyramid
        def can_build_pyramid(row):
            if len(row) == 1:
                return True

            # Generate all possible next rows
            next_row = []
            for i in range(len(row) - 1):
                pair = row[i:i+2]
                if pair in allowed_map:
                    next_row.append(allowed_map[pair])
                else:
                    return False

            # Try all combinations of the next row
            def backtrack(index, current_row):
                if index == len(next_row):
                    return can_build_pyramid(current_row)

                for block in next_row[index]:
                    if backtrack(index + 1, current_row + block):
                        return True
                return False

            return backtrack(0, "")

        # Start the process with the bottom row
        return can_build_pyramid(bottom)


def test_pyramid_transition():
    solution = Solution()

    # Test case 1: Basic successful case
    bottom1 = "BCD"
    allowed1 = ["BCG", "CDE", "GEF", "FED"]
    result1 = solution.pyramidTransition(bottom1, allowed1)
    assert result1 == True, f"Test case 1 failed. Expected True, got {result1}"
    print(
        f"Test case 1 passed: bottom={bottom1}, allowed={allowed1}, result={result1}")

    # Test case 2: Impossible case
    bottom2 = "AABA"
    allowed2 = ["AAA", "AAB", "ABA", "ABB", "BAC"]
    result2 = solution.pyramidTransition(bottom2, allowed2)
    assert result2 == False, f"Test case 2 failed. Expected False, got {result2}"
    print(
        f"Test case 2 passed: bottom={bottom2}, allowed={allowed2}, result={result2}")

    # Test case 3: Single character case
    bottom3 = "A"
    allowed3 = ["AAA"]
    result3 = solution.pyramidTransition(bottom3, allowed3)
    assert result3 == True, f"Test case 3 failed. Expected True, got {result3}"
    print(
        f"Test case 3 passed: bottom={bottom3}, allowed={allowed3}, result={result3}")

    # Test case 4: Multiple valid paths
    bottom4 = "ABC"
    allowed4 = ["ABD", "BCE", "DEF", "ABC"]
    result4 = solution.pyramidTransition(bottom4, allowed4)
    assert result4 == True, f"Test case 4 failed. Expected True, got {result4}"
    print(
        f"Test case 4 passed: bottom={bottom4}, allowed={allowed4}, result={result4}")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_pyramid_transition()
