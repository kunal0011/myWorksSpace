"""
LeetCode 277 - Find the Celebrity

Problem Statement:
Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may be one celebrity. 
The definition of a celebrity is that all the other n - 1 people know them but they don't know any others.

You are given a helper function: knows(a, b) which returns True if person a knows person b, else False.
Implement a function to find the celebrity. If there is no celebrity, return -1.

Logic:
1. Use two-pointer approach to find a candidate
   - If a knows b, a can't be celebrity, move a forward
   - If a doesn't know b, b can't be celebrity, move b backward
2. Verify the candidate by checking:
   - Candidate doesn't know anyone else
   - Everyone else knows the candidate
"""

def knows(a: int, b: int) -> bool:
    # This is a mock implementation for testing
    # In real leetcode environment, this is provided
    relations = {
        (0, 1): True, (0, 2): False,
        (1, 0): False, (1, 2): True,
        (2, 0): False, (2, 1): False
    }
    return relations.get((a, b), False)


class Solution:
    def findCelebrity(self, n: int) -> int:
        # Step 1: Find the candidate for celebrity
        left, right = 0, n - 1

        while left < right:
            if knows(left, right):
                # left cannot be a celebrity, move left pointer
                left += 1
            else:
                # right cannot be a celebrity, move right pointer
                right -= 1

        # Step 2: Verify if the candidate is actually a celebrity
        candidate = left

        # Check if the candidate is known by everyone
        for i in range(n):
            if i != candidate:
                if knows(candidate, i) or not knows(i, candidate):
                    return -1  # Candidate is not a celebrity

        return candidate


def test_find_celebrity():
    solution = Solution()
    
    # Test cases
    test_cases = [
        (3, 2),    # Example with celebrity (person 2)
        (2, -1),   # Example with no celebrity
        (1, 0),    # Single person case
    ]
    
    for i, (n, expected) in enumerate(test_cases):
        result = solution.findCelebrity(n)
        assert result == expected, f"Test case {i + 1} failed: expected {expected}, got {result}"
        print(f"Test case {i + 1} passed: n={n}, celebrity={result}")

if __name__ == "__main__":
    test_find_celebrity()
    print("All test cases passed!")
