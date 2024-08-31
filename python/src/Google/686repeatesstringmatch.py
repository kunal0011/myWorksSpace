class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        # Calculate minimum number of repetitions needed
        # This is equivalent to math.ceil(len(B) / len(A))
        repeat_count = -(-len(B) // len(A))

        # Create a string with `repeat_count` repetitions of A
        repeated_A = A * repeat_count

        # Check if B is a substring of the repeated string
        if B in repeated_A:
            return repeat_count

        # Check if B is a substring of the repeated string with one additional repetition
        if B in (repeated_A + A):
            return repeat_count + 1

        return -1


# Example usage
solution = Solution()
A1 = "abcd"
B1 = "cdabcdab"

A2 = "a"
B2 = "aa"

print(solution.repeatedStringMatch(A1, B1))  # Output: 3
print(solution.repeatedStringMatch(A2, B2))  # Output: 2
