from collections import defaultdict


class Solution:
    def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:
        # Create a dictionary where key is a pair (A, B) and value is a list of all C's
        transitions = defaultdict(list)
        for triple in allowed:
            transitions[triple[:2]].append(triple[2])

        # Memoization to store the results of subproblems
        memo = {}

        # Recursive function to check if we can build the pyramid from the current row
        def can_build(row):
            # If we reach a row with only one block, the pyramid is built successfully
            if len(row) == 1:
                return True

            # Memoization check
            if row in memo:
                return memo[row]

            # Try to build the next row
            for next_row in build_next_row(row, 0, []):
                if can_build(next_row):
                    memo[row] = True
                    return True

            memo[row] = False
            return False

        # Helper function to build all possible next rows
        def build_next_row(row, i, current):
            if i == len(row) - 1:
                yield "".join(current)
            else:
                pair = row[i:i + 2]
                if pair in transitions:
                    for block in transitions[pair]:
                        current.append(block)
                        yield from build_next_row(row, i + 1, current)
                        current.pop()

        # Start recursion from the bottom row
        return can_build(bottom)


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    bottom1 = "BCD"
    allowed1 = ["BCG", "CDE", "GEA", "FFF"]
    print(sol.pyramidTransition(bottom1, allowed1))  # Expected output: True

    # Test case 2
    bottom2 = "AABA"
    allowed2 = ["AAA", "AAB", "ABA", "ABB", "BAC"]
    print(sol.pyramidTransition(bottom2, allowed2))  # Expected output: False
