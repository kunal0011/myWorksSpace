"""
LeetCode 461: Hamming Distance

Problem Statement:
The Hamming distance between two integers is the number of positions at which the 
corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.

Constraints:
- 0 <= x, y <= 2^31 - 1
"""


def hammingDistance(x: int, y: int) -> int:
    # XOR the numbers and count the 1's in the result
    xor = x ^ y
    count = 0

    # Count set bits in XOR result
    while xor:
        count += xor & 1
        xor >>= 1

    return count

# Alternative solution using built-in bin() function


def hammingDistance_alt(x: int, y: int) -> int:
    return bin(x ^ y).count('1')

# Test driver


def run_tests():
    test_cases = [
        {
            "x": 1,
            "y": 4,
            "expected": 2,
            "explanation": "1 (0001) and 4 (0100) differ at positions 0 and 2"
        },
        {
            "x": 3,
            "y": 1,
            "expected": 1,
            "explanation": "3 (0011) and 1 (0001) differ at position 1"
        },
        {
            "x": 0,
            "y": 0,
            "expected": 0,
            "explanation": "No differing bits"
        },
        {
            "x": 15,
            "y": 0,
            "expected": 4,
            "explanation": "15 (1111) and 0 (0000) differ at all positions"
        }
    ]

    for i, test in enumerate(test_cases, 1):
        # Test both implementations
        result = hammingDistance(test["x"], test["y"])
        alt_result = hammingDistance_alt(test["x"], test["y"])

        status = "PASSED" if result == test["expected"] else "FAILED"
        print(f"Test {i}: {status}")
        print(f"Input: x = {test['x']} ({bin(test['x'])[2:].zfill(4)}), "
              f"y = {test['y']} ({bin(test['y'])[2:].zfill(4)})")
        print(f"Expected: {test['expected']}")
        print(f"Got: {result} (alternate method: {alt_result})")
        print(f"Explanation: {test['explanation']}\n")


if __name__ == "__main__":
    print("Running test cases for Hamming Distance problem:\n")
    run_tests()

"""
Solution Logic Explanation:

1. Optimal Bit Manipulation Approach:
   - XOR the two numbers to get 1's at differing bit positions
   - Count the number of 1's in the XOR result
   - Each 1 represents a position where bits differ

2. Implementation Details:
   - Use XOR (^) to identify differing bits
   - Use bit shifting and AND operations to count set bits
   - Time Complexity: O(1) as integers are fixed size
   - Space Complexity: O(1)

3. Alternative Approach:
   - Use Python's built-in bin() to convert to binary string
   - Count '1' characters in the binary representation
   - Less efficient but more readable
"""
