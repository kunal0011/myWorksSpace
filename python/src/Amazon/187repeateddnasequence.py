"""
LeetCode 187. Repeated DNA Sequences

Problem Statement:
All DNA is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.
Given a DNA string s, return all the 10-letter-long sequences (substrings) that occur more than once
in a DNA molecule.

Example 1:
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC", "CCCCCAAAAA"]

Example 2:
Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]

Constraints:
- 1 <= s.length <= 10^5
- s[i] is either 'A', 'C', 'G', or 'T'.
"""

from typing import List, Tuple, Dict


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        """
        Find all 10-letter-long sequences that occur more than once.
        Time complexity: O(n) where n is the length of the string s.
        Space complexity: O(n)
        """
        if len(s) < 10:
            return []

        seen = {}
        repeated = set()

        for i in range(len(s) - 9):
            substring = s[i:i+10]
            if substring in seen:
                repeated.add(substring)
            else:
                seen[substring] = 1

        return list(repeated)

    def findRepeatedDnaSequencesWithSteps(self, s: str) -> Tuple[List[str], List[Dict]]:
        """
        Find repeated DNA sequences with detailed step tracking.
        Returns a tuple of (result, steps) where steps is a list of dictionaries
        describing each action.

        Time complexity: O(n)
        Space complexity: O(n)
        """
        steps = []
        if len(s) < 10:
            steps.append({
                "action": "Early return",
                "reason": "Input string length is less than 10",
                "result": []
            })
            return [], steps

        seen = {}
        repeated = set()

        steps.append({
            "action": "Initialization",
            "message": "Created empty dictionary for seen sequences and an empty set for repeated sequences"
        })

        for i in range(len(s) - 9):
            substring = s[i:i+10]
            action_details = {
                "action": "Process substring",
                "index": i,
                "substring": substring
            }
            if substring in seen:
                repeated.add(substring)
                action_details["result"] = "Repeated substring found"
            else:
                seen[substring] = 1
                action_details["result"] = "First occurrence"
            steps.append(action_details)

        final_result = list(repeated)
        steps.append({
            "action": "Final result",
            "repeated_subsequences": final_result
        })

        return final_result, steps


def visualize_steps(steps: List[Dict]) -> None:
    """Helper function to visualize the step tracking of the algorithm."""
    print("\nStep-by-Step Tracking:")
    for i, step in enumerate(steps, 1):
        print(f"\nStep {i}: {step['action']}")
        for key, value in step.items():
            if key != "action":
                print(f"  {key}: {value}")


def test_repeated_dna_sequences():
    """
    Test function with various test cases.
    """
    test_cases = [
        {
            "s": "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
            "expected": sorted(["AAAAACCCCC", "CCCCCAAAAA"]),
            "description": "Basic example with two repeated 10-letter sequences"
        },
        {
            "s": "AAAAAAAAAAAAA",
            "expected": sorted(["AAAAAAAAAA"]),
            "description": "String with overlapping repeats"
        },
        {
            "s": "ACGT",
            "expected": [],
            "description": "String shorter than 10 characters"
        }
    ]

    solution = Solution()

    for i, test_case in enumerate(test_cases, 1):
        s = test_case["s"]
        expected = test_case["expected"]
        print(f"\n{'='*80}")
        print(f"Test Case {i}: {test_case['description']}")
        print(f"Input string: {s}")

        # Test basic implementation
        result = solution.findRepeatedDnaSequences(s)
        result_sorted = sorted(result)
        print(f"Output (basic): {result_sorted}")
        assert result_sorted == expected, f"Expected {expected}, got {result_sorted}"

        # Test step-by-step implementation
        result_steps, steps = solution.findRepeatedDnaSequencesWithSteps(s)
        result_steps_sorted = sorted(result_steps)
        print(f"Output (with steps): {result_steps_sorted}")
        assert result_steps_sorted == expected, f"Expected {expected}, got {result_steps_sorted}"

        # Visualize steps for the first test case for clarity
        if i == 1:
            visualize_steps(steps)

        print("✓ Test case passed!")

    print("\nAll test cases passed! 🎉")


if __name__ == "__main__":
    test_repeated_dna_sequences()
