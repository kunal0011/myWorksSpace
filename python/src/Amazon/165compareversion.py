"""
LeetCode 165. Compare Version Numbers

Problem Statement:
Given two version numbers, version1 and version2, compare them.

Version numbers consist of one or more revisions joined by a dot '.'. Each revision consists of digits 
and may contain leading zeros. Every revision contains at least one character. Revisions are 0-indexed 
from left to right, with the leftmost revision being revision 0, the next revision being revision 1, 
and so on.

Return:
* 1 if version1 > version2
* -1 if version1 < version2
* 0 if version1 == version2

Example 1:
Input: version1 = "1.01", version2 = "1.001"
Output: 0
Explanation: Ignoring leading zeros, both "01" and "001" represent the same integer "1"

Example 2:
Input: version1 = "1.0", version2 = "1.0.0"
Output: 0
Explanation: version1 does not specify revision 2, which means it is treated as "0"

Example 3:
Input: version1 = "0.1", version2 = "1.1"
Output: -1
Explanation: version1's revision 0 is "0", while version2's revision 0 is "1". 0 < 1, so version1 < version2

Constraints:
- 1 <= version1.length, version2.length <= 500
- version1 and version2 only contain digits and '.'
- version1 and version2 are valid version numbers
- All revisions in version1 and version2 can be stored in a 32-bit integer
"""

from typing import List, Tuple


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        """
        Compare two version numbers.
        Time complexity: O(max(n,m)) where n,m are lengths of input strings
        Space complexity: O(n+m)
        """
        v1 = [int(v) for v in version1.split('.')]
        v2 = [int(v) for v in version2.split('.')]

        # Make lengths equal by padding with zeros
        max_length = max(len(v1), len(v2))
        v1 += [0] * (max_length - len(v1))
        v2 += [0] * (max_length - len(v2))

        for i in range(max_length):
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1

        return 0

    def compareVersionWithSteps(self, version1: str, version2: str) -> Tuple[int, List[dict]]:
        """
        Compare versions with detailed steps.
        Time complexity: O(max(n,m))
        Space complexity: O(n+m)
        """
        steps = []

        # Split versions into components
        v1 = [int(v) for v in version1.split('.')]
        v2 = [int(v) for v in version2.split('.')]

        steps.append({
            "action": "Split versions",
            "v1_components": v1.copy(),
            "v2_components": v2.copy()
        })

        # Pad with zeros
        max_length = max(len(v1), len(v2))
        original_v1_len = len(v1)
        original_v2_len = len(v2)

        v1 += [0] * (max_length - len(v1))
        v2 += [0] * (max_length - len(v2))

        if len(v1) > original_v1_len or len(v2) > original_v2_len:
            steps.append({
                "action": "Pad versions",
                "v1_padded": v1.copy(),
                "v2_padded": v2.copy()
            })

        # Compare components
        for i in range(max_length):
            steps.append({
                "action": "Compare components",
                "index": i,
                "v1_component": v1[i],
                "v2_component": v2[i]
            })

            if v1[i] > v2[i]:
                steps.append({
                    "action": "Result",
                    "result": 1,
                    "reason": f"v1[{i}] > v2[{i}]"
                })
                return 1, steps
            elif v1[i] < v2[i]:
                steps.append({
                    "action": "Result",
                    "result": -1,
                    "reason": f"v1[{i}] < v2[{i}]"
                })
                return -1, steps

        steps.append({
            "action": "Result",
            "result": 0,
            "reason": "Versions are equal"
        })
        return 0, steps


def visualize_steps(version1: str, version2: str, steps: List[dict]) -> None:
    """Helper function to visualize comparison steps."""
    print("\nComparison Steps:")
    for i, step in enumerate(steps, 1):
        print(f"\nStep {i}: {step['action']}")

        if step['action'] == "Split versions":
            print(f"Version 1 components: {step['v1_components']}")
            print(f"Version 2 components: {step['v2_components']}")

        elif step['action'] == "Pad versions":
            print(f"Version 1 padded: {step['v1_padded']}")
            print(f"Version 2 padded: {step['v2_padded']}")

        elif step['action'] == "Compare components":
            print(f"Comparing index {step['index']}:")
            print(f"v1[{step['index']}] = {step['v1_component']}")
            print(f"v2[{step['index']}] = {step['v2_component']}")

        elif step['action'] == "Result":
            print(f"Result: {step['result']}")
            print(f"Reason: {step['reason']}")


def test_compare_version():
    """
    Test function with various test cases.
    """
    test_cases = [
        {
            "version1": "1.01",
            "version2": "1.001",
            "expected": 0,
            "description": "Leading zeros"
        },
        {
            "version1": "1.0",
            "version2": "1.0.0",
            "expected": 0,
            "description": "Different lengths"
        },
        {
            "version1": "0.1",
            "version2": "1.1",
            "expected": -1,
            "description": "Different major versions"
        },
        {
            "version1": "1.0.1",
            "version2": "1",
            "expected": 1,
            "description": "Missing minor versions"
        },
        {
            "version1": "7.5.2.4",
            "version2": "7.5.3",
            "expected": -1,
            "description": "Complex versions"
        }
    ]

    solution = Solution()

    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{'='*80}")
        print(f"Test Case {i}: {test_case['description']}")
        print(f"Version 1: {test_case['version1']}")
        print(f"Version 2: {test_case['version2']}")

        # Test both implementations
        result1 = solution.compareVersion(
            test_case['version1'], test_case['version2'])
        result2, steps = solution.compareVersionWithSteps(
            test_case['version1'], test_case['version2'])

        print(f"\nResults:")
        print(f"Comparison result: {result1}")

        visualize_steps(test_case['version1'], test_case['version2'], steps)

        assert result1 == test_case['expected'], \
            f"Basic approach failed. Expected {test_case['expected']}, got {result1}"
        assert result2 == test_case['expected'], \
            f"Step tracking failed. Expected {test_case['expected']}, got {result2}"

        print("✓ Test case passed!")

    print("\nAll test cases passed! 🎉")


if __name__ == "__main__":
    test_compare_version()
