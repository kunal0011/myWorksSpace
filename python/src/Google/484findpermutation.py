"""
LeetCode 484: Find Permutation

Problem Statement:
A permutation perm of n integers of all the integers in the range [1, n] can be represented
as a string s of length n - 1 where:
- s[i] == 'I' if perm[i] < perm[i + 1], and
- s[i] == 'D' if perm[i] > perm[i + 1]

Given a string s, reconstruct the lexicographically smallest permutation perm that matches s.

Constraints:
- 1 <= s.length <= 10^5
- s[i] is either 'I' or 'D'
"""


def findPermutation(s: str) -> list[int]:
    n = len(s)
    result = []
    stack = []

    # Push numbers onto stack for consecutive 'D's and pop for 'I'
    curr_num = 1

    for i in range(n):
        stack.append(curr_num)
        curr_num += 1

        # If we see 'I', pop everything from stack
        if s[i] == 'I':
            while stack:
                result.append(stack.pop())

    # Push last number and clear stack
    stack.append(curr_num)
    while stack:
        result.append(stack.pop())

    return result


def validate_permutation(perm: list[int], s: str) -> bool:
    """Helper function to validate if permutation matches the pattern"""
    for i in range(len(s)):
        if (s[i] == 'I' and perm[i] >= perm[i + 1]) or \
           (s[i] == 'D' and perm[i] <= perm[i + 1]):
            return False
    return True

# Test driver


def run_tests():
    test_cases = [
        {
            "s": "I",
            "expected": [1, 2],
            "explanation": "The permutation [1,2] has one increase as required"
        },
        {
            "s": "DI",
            "expected": [2, 1, 3],
            "explanation": "The permutation [2,1,3] has a decrease then an increase"
        },
        {
            "s": "DDIID",
            "expected": [3, 2, 1, 4, 6, 5],
            "explanation": "Complex pattern with multiple increases and decreases"
        },
        {
            "s": "III",
            "expected": [1, 2, 3, 4],
            "explanation": "Strictly increasing sequence"
        }
    ]

    for i, test in enumerate(test_cases, 1):
        result = findPermutation(test["s"])
        is_valid = validate_permutation(result, test["s"])
        expected_valid = validate_permutation(test["expected"], test["s"])

        # Check if result is valid and lexicographically smallest possible
        status = "PASSED" if is_valid and result == test["expected"] else "FAILED"

        print(f"Test {i}: {status}")
        print(f"Pattern: {test['s']}")
        print(f"Expected: {test['expected']}")
        print(f"Got: {result}")
        print(f"Valid permutation: {is_valid}")
        print(f"Explanation: {test['explanation']}\n")


if __name__ == "__main__":
    print("Running test cases for Find Permutation problem:\n")
    run_tests()

"""
Solution Logic Explanation:

1. Key Insight:
   - Use a stack to handle consecutive 'D's
   - When we see an 'I', we need to reverse the decreasing sequence

2. Algorithm Steps:
   - Process string from left to right
   - Push numbers onto stack for 'D's
   - When we hit 'I', pop everything from stack
   - Continue until end of string
   - Clear remaining stack

3. Why it works:
   - Stack naturally reverses decreasing sequences
   - Always uses smallest available numbers
   - Guarantees lexicographically smallest result

4. Time and Space Complexity:
   - Time: O(n) where n is length of string
   - Space: O(n) for stack and result array

Example:
For pattern "DI":
1. Push 1 for 'D' -> stack=[1]
2. Push 2 -> stack=[1,2]
3. Pop all for 'I' -> result=[2,1]
4. Push and pop 3 -> result=[2,1,3]
"""
