class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # Convert J to a set for O(1) lookups
        jewels = set(J)
        # Count how many stones in S are also jewels
        return sum(s in jewels for s in S)


# Example usage
solution = Solution()
J1 = "aA"
S1 = "aAAbbbb"

J2 = "z"
S2 = "ZZ"

print(solution.numJewelsInStones(J1, S1))  # Output: 3
print(solution.numJewelsInStones(J2, S2))  # Output: 0
