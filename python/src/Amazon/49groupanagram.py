from collections import defaultdict
from typing import List

"""
LeetCode 49. Group Anagrams

Problem Statement:
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
- 1 <= strs.length <= 104
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Use defaultdict to automatically initialize empty lists
        anagram_groups = defaultdict(list)

        # Group strings by sorted version as key
        for s in strs:
            # Convert string to tuple of character counts
            # This is more efficient than sorting for strings
            char_count = [0] * 26
            for c in s:
                char_count[ord(c) - ord('a')] += 1

            # Use tuple as key (lists can't be dictionary keys)
            anagram_groups[tuple(char_count)].append(s)

        # Return all groups
        return list(anagram_groups.values())


def explain_grouping(strs: List[str]) -> None:
    """
    Function to explain the anagram grouping process step by step
    """
    print(f"\nGrouping anagrams for: {strs}")
    print("=" * 50)

    anagram_groups = defaultdict(list)

    for s in strs:
        # Show character counting process
        print(f"\nProcessing string: '{s}'")

        char_count = [0] * 26
        print("Counting characters:")
        for c in s:
            index = ord(c) - ord('a')
            char_count[index] += 1
            print(f"  '{c}' -> index {index}, count: {char_count[index]}")

        key = tuple(char_count)
        anagram_groups[key].append(s)
        print(f"Current groups after adding '{s}':")
        for group in anagram_groups.values():
            print(f"  {group}")

    result = list(anagram_groups.values())
    print("\nFinal grouping:")
    for group in result:
        print(group)

    return result


def test_group_anagrams():
    """
    Test function to verify the solution with various test cases
    """
    solution = Solution()

    test_cases = [
        {
            "strs": ["eat", "tea", "tan", "ate", "nat", "bat"],
            "expected": [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
            "description": "Basic case with multiple groups"
        },
        {
            "strs": [""],
            "expected": [[""]],
            "description": "Empty string"
        },
        {
            "strs": ["a"],
            "expected": [["a"]],
            "description": "Single character"
        },
        {
            "strs": ["abc", "cba", "bac", "cab", "acb", "bca"],
            "expected": [["abc", "cba", "bac", "cab", "acb", "bca"]],
            "description": "All anagrams"
        },
        {
            "strs": ["abc", "def", "ghi"],
            "expected": [["abc"], ["def"], ["ghi"]],
            "description": "No anagrams"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        strs = test_case["strs"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print(f"Input: strs = {strs}")

        result = solution.groupAnagrams(strs.copy())

        # Sort for comparison
        result_sorted = sorted([sorted(group) for group in result])
        expected_sorted = sorted([sorted(group) for group in expected])

        assert result_sorted == expected_sorted, \
            f"\nTest case {i} failed!\nExpected: {expected}\nGot: {result}"
        print(f"✓ Test case {i} passed!")


if __name__ == "__main__":
    try:
        test_group_anagrams()
        print("\nAll test cases passed successfully! 🎉")

        # Explain with detailed examples
        explain_grouping(["eat", "tea", "tan", "ate", "nat", "bat"])
        explain_grouping(["abc", "cba", "def"])
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
