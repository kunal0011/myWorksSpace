"""
LeetCode 38 - Count and Say

Problem Statement:
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
- countAndSay(1) = "1"
- countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), 
  which is then converted into a different digit string.

To determine how you "say" a digit string, split it into the minimal number of substrings 
such that each substring contains exactly one unique digit. Then for each substring, say 
the number of digits, followed by the digit. Finally, concatenate every said digit.

Example:
1 is read off as "one 1" or 1 1
11 is read off as "two 1s" or 2 1
21 is read off as "one 2, one 1" or 1 2 1 1
1211 is read off as "one 1, one 2, two 1s" or 1 1 1 2 2 1

Time Complexity: O(2^n) in worst case
Space Complexity: O(2^n) in worst case
"""

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        # Get the previous term
        prev = self.countAndSay(n - 1)
        
        result = []
        count = 1
        current = prev[0]
        
        # Process the previous term
        for i in range(1, len(prev)):
            if prev[i] == current:
                count += 1
            else:
                result.extend([str(count), current])
                current = prev[i]
                count = 1
        
        # Add the last group
        result.extend([str(count), current])
        
        return "".join(result)


def test_count_and_say():
    solution = Solution()
    
    # Test cases
    test_cases = [
        (1, "1"),
        (2, "11"),
        (3, "21"),
        (4, "1211"),
        (5, "111221"),
        (6, "312211"),
        (7, "13112221"),
        (8, "1113213211"),
    ]
    
    for i, (n, expected) in enumerate(test_cases, 1):
        result = solution.countAndSay(n)
        print(f"Test case {i}:")
        print(f"n = {n}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"Pass: {result == expected}\n")
        
        # Additional validation for format
        if not result.isdigit():
            print(f"Error: Result should only contain digits! Got {result}")


if __name__ == "__main__":
    test_count_and_say()