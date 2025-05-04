"""
LeetCode 763: Partition Labels

Problem Statement:
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.
Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.
Return a list of integers representing the size of these parts.

Logic:
1. Find the last occurrence of each character in the string using dictionary
2. Traverse the string and for each character:
   - Update partition end to max of current end and last occurrence of current char
   - When current index reaches partition end, we've found a valid partition
   - Add partition length to result and update start position
3. Return list of partition lengths

Time Complexity: O(n) where n is length of string
Space Complexity: O(1) since we store at most 26 characters (lowercase English letters)
"""

from typing import List


class Solution:
    def partitionLabels(self, S: str):
        # Step 1: Create a dictionary to store the last occurrence of each character
        last_occurrence = {c: i for i, c in enumerate(S)}

        # Step 2: Traverse the string to create partitions
        partitions = []
        start, end = 0, 0

        for i, c in enumerate(S):
            # Update the end to the farthest last occurrence of the current character
            end = max(end, last_occurrence[c])

            # If the current index reaches the end of the partition
            if i == end:
                partitions.append(end - start + 1)
                start = i + 1

        return partitions


def test_partition_labels():
    solution = Solution()

    # Test case 1: Given example
    s1 = "ababcbacadefegdehijhklij"
    result1 = solution.partitionLabels(s1)
    assert result1 == [
        9, 7, 8], f"Test case 1 failed. Expected [9, 7, 8], got {result1}"
    print(f"Test case 1 passed:\nInput: {s1}\nOutput: {result1}")

    # Test case 2: Single character
    s2 = "a"
    result2 = solution.partitionLabels(s2)
    assert result2 == [1], f"Test case 2 failed. Expected [1], got {result2}"
    print(f"\nTest case 2 passed:\nInput: {s2}\nOutput: {result2}")

    # Test case 3: All same characters
    s3 = "aaaa"
    result3 = solution.partitionLabels(s3)
    assert result3 == [4], f"Test case 3 failed. Expected [4], got {result3}"
    print(f"\nTest case 3 passed:\nInput: {s3}\nOutput: {result3}")

    # Test case 4: No overlapping characters
    s4 = "abcd"
    result4 = solution.partitionLabels(s4)
    assert result4 == [
        1, 1, 1, 1], f"Test case 4 failed. Expected [1, 1, 1, 1], got {result4}"
    print(f"\nTest case 4 passed:\nInput: {s4}\nOutput: {result4}")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_partition_labels()
