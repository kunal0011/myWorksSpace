"""
LeetCode 466 - Count The Repetitions

Problem Statement:
-----------------
Define str = [s, n] as the string str that consists of the string s concatenated n times.
- For example, str == ["abc", 3] == "abcabcabc".

We are given two strings s1 and s2 and two integers n1 and n2. Find the maximum integer m 
such that str == [s2, m] is a substring of str == [s1, n1].

Key Points:
----------
1. Need to find how many times s2 repeats in s1's repetitions
2. Direct simulation might exceed time limit
3. Need to detect cycles in pattern matching
4. Handle edge cases where s2 contains chars not in s1
5. Optimize using pattern recognition

Examples:
--------
Input: s1 = "acb", n1 = 4, s2 = "ab", n2 = 2
Output: 2
Explanation:
- str1 = [s1, n1] = "acbacbacbacb"
- str2 = [s2, n2] = "abab"
- str2 can be repeated 2 times in str1

Input: s1 = "acb", n1 = 1, s2 = "acb", n2 = 1
Output: 1

Constraints:
-----------
* 1 <= s1.length, s2.length <= 100
* 1 <= n1, n2 <= 10^6
* s1 and s2 consist of lowercase English letters
"""

class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        """
        Calculate maximum number of times s2 repeats in s1's repetitions.
        
        Algorithm:
        1. First check if all chars in s2 exist in s1
        2. Track positions in both strings and count repetitions
        3. Detect cycles to handle large n1 efficiently
        4. Use cycle information to calculate final count
        
        Time Complexity: O(len(s1) * unique_positions_in_s2)
        Space Complexity: O(len(s2)) for recall dictionary
        """
        # Early exit if s2 contains chars not in s1
        if not set(s2).issubset(set(s1)):
            return 0

        # Initialize counters and tracking variables
        s1_count = 0  # Number of s1 strings processed
        s2_count = 0  # Number of complete s2 strings found
        index_s2 = 0  # Current position in s2
        recall = {}   # Maps s2 position to (s1_count, s2_count) for cycle detection

        while s1_count < n1:
            # Process each character in s1
            for char in s1:
                # If current char matches current position in s2
                if char == s2[index_s2]:
                    index_s2 += 1
                    # If we complete s2, reset index and increment count
                    if index_s2 == len(s2):
                        s2_count += 1
                        index_s2 = 0

            s1_count += 1

            # Check for cycle based on current position in s2
            if index_s2 in recall:
                # Get previous counts when we were at this position
                prev_s1_count, prev_s2_count = recall[index_s2]
                
                # Calculate cycle lengths
                cycle_s1 = s1_count - prev_s1_count
                cycle_s2 = s2_count - prev_s2_count

                # Calculate remaining full cycles
                remaining_s1 = n1 - s1_count
                cycles = remaining_s1 // cycle_s1

                # Apply cycles to counts
                s1_count += cycles * cycle_s1
                s2_count += cycles * cycle_s2
            else:
                # Record current state for cycle detection
                recall[index_s2] = (s1_count, s2_count)

        # Return number of complete s2 groups
        return s2_count // n2


def test_get_max_repetitions():
    """
    Test driver for count the repetitions problem
    """
    test_cases = [
        (
            "acb", 4, "ab", 2,
            2,  # Basic case with repetition
            "Can find 'abab' twice in 'acbacbacbacb'"
        ),
        (
            "acb", 1, "acb", 1,
            1,  # Exact match case
            "Single exact match"
        ),
        (
            "aaa", 3, "aa", 1,
            4,  # Multiple matches possible
            "Can find 'aa' four times in 'aaaaaaaaa'"
        ),
        (
            "abc", 4, "xyz", 2,
            0,  # No match possible
            "s2 contains characters not in s1"
        ),
        (
            "aaa", 1000000, "a", 1000,
            1000,  # Large input with cycle
            "Tests cycle detection with large numbers"
        ),
        (
            "phqghumeaylnlfdxfircvscxggbwkfnqduxwfnfozvsrtkjprepggxrpnrvystmwcysyycqpevikef",
            1000000,
            "foobar",
            1000,
            0,  # Complex string with no matches
            "Complex string test with no possible matches"
        ),
        (
            "bacaba", 3, "aba", 1,
            2,  # Overlapping pattern
            "Pattern can be found in overlapping positions"
        ),
        (
            "aahumeaylnlfdxfi", 1000000, "aaa", 1000,
            0,  # Long string with impossible pattern
            "Long string where pattern is impossible to match completely"
        )
    ]
    
    solution = Solution()
    
    for i, (s1, n1, s2, n2, expected, description) in enumerate(test_cases, 1):
        result = solution.getMaxRepetitions(s1, n1, s2, n2)
        status = "PASSED" if result == expected else "FAILED"
        print(f"\nTest case {i}: {status}")
        print(f"Description: {description}")
        print(f"Input:")
        print(f"s1 = '{s1}', n1 = {n1}")
        print(f"s2 = '{s2}', n2 = {n2}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        if result != expected:
            print(f"Note: Check cycle detection and edge cases")
        print("-" * 40)

if __name__ == "__main__":
    test_get_max_repetitions()
