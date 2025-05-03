"""
LeetCode 481: Magical String

Problem Statement:
A magical string s consists of only '1' and '2' and obeys the following rules:
- The string s is magical because concatenating the number of contiguous occurrences 
  of characters '1' and '2' generates the string s itself.
- The first few elements of s is s = "1221121221221121122......"
- If we group the consecutive 1's and 2's in s, it will be "1 22 11 2 1 22 1 22 11 2 11 22 ......"
  and the occurrences of 1's or 2's in each group are "1 2 2 1 1 2 1 2 2 1 2 2 ......"

Return the number of 1's in the first n number of digits in the magical string s.

Constraints:
- 1 <= n <= 10^5
"""


def magicalString(n: int) -> int:
    if n == 0:
        return 0
    if n <= 3:
        return 1

    # Initialize the magical string with the first 3 elements
    s = [1, 2, 2]
    count = 1  # Count of 1's (first element is 1)
    head = 2   # Index to read from

    # Generate string up to length n
    while len(s) < n:
        # Current value to append (alternate between 1 and 2)
        curr = 1 if s[-1] == 2 else 2

        # Number of times to append curr
        times = s[head]

        # Append curr the required number of times
        for _ in range(times):
            s.append(curr)
            if curr == 1 and len(s) <= n:
                count += 1

        head += 1

    return count

# Test driver


def run_tests():
    test_cases = [
        {
            "n": 6,
            "expected": 3,
            "explanation": "First 6 digits are '122112', which contains three 1's"
        },
        {
            "n": 1,
            "expected": 1,
            "explanation": "First digit is '1'"
        },
        {
            "n": 4,
            "expected": 2,
            "explanation": "First 4 digits are '1221', which contains two 1's"
        },
        {
            "n": 10,
            "expected": 5,
            "explanation": "First 10 digits are '1221121122', which contains five 1's"
        }
    ]

    for i, test in enumerate(test_cases, 1):
        result = magicalString(test["n"])
        status = "PASSED" if result == test["expected"] else "FAILED"
        print(f"Test {i}: {status}")
        print(f"Input n: {test['n']}")
        print(f"Expected: {test['expected']}")
        print(f"Got: {result}")
        print(f"Explanation: {test['explanation']}\n")


if __name__ == "__main__":
    print("Running test cases for Magical String problem:\n")
    run_tests()

"""
Solution Logic Explanation:

1. Key Insight:
   - Each group's length is determined by the sequence itself
   - The values alternate between 1 and 2
   - We only need to generate up to n elements

2. Algorithm Steps:
   - Start with initial sequence [1,2,2]
   - Use a pointer (head) to read group lengths
   - Alternate between appending 1's and 2's
   - Keep track of number of 1's seen

3. Time and Space Complexity:
   - Time: O(n) to generate n elements
   - Space: O(n) to store the sequence

4. Optimizations:
   - Only count 1's within first n elements
   - Early return for small n values
   - No need to store full string, could use array/list
"""
