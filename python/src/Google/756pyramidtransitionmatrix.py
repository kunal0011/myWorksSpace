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


# Example usage
solution = Solution()
bottom1 = "BCD"
allowed1 = ["BCG", "CDE", "GEA", "FFF"]

bottom2 = "AABA"
allowed2 = ["AAA", "AAB", "ABA", "ABB", "BAC"]

print(solution.pyramidTransition(bottom1, allowed1))  # Output: True
print(solution.pyramidTransition(bottom2, allowed2))  # Output: False
