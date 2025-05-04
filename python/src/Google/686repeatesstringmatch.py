"""
LeetCode 686: Repeated String Match
Problem Statement:
Given two strings a and b, return the minimum number of times you should repeat string a 
so that string b is a substring of the repeated string. If it's impossible, return -1.

Logic:
1. Calculate minimum repetitions needed = ceil(len(B)/len(A))
2. Create repeated string with minimum repetitions
3. Check if B is substring of repeated string
4. If not, try one more repetition (to handle edge cases)
5. If still not found, return -1

Time Complexity: O(N) where N is len(A) * repeat_count
Space Complexity: O(N) for storing repeated string
"""


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


def test_repeated_string_match():
    solution = Solution()

    # Test Case 1: Normal case
    assert solution.repeatedStringMatch("abcd", "cdabcdab") == 3
    print("Test case 1: 'abcd' repeated to contain 'cdabcdab' ✓")

    # Test Case 2: Simple repetition
    assert solution.repeatedStringMatch("a", "aa") == 2
    print("Test case 2: 'a' repeated to contain 'aa' ✓")

    # Test Case 3: Impossible case
    assert solution.repeatedStringMatch("abc", "wxyz") == -1
    print("Test case 3: 'abc' cannot contain 'wxyz' ✓")

    # Test Case 4: Single repetition
    assert solution.repeatedStringMatch("abc", "abc") == 1
    print("Test case 4: 'abc' needs no repetition to contain 'abc' ✓")

    # Test Case 5: Empty strings
    assert solution.repeatedStringMatch("", "abc") == -1
    print("Test case 5: Empty string cannot contain 'abc' ✓")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_repeated_string_match()
