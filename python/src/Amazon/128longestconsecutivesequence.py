"""
LeetCode 128. Longest Consecutive Sequence

Problem Statement:
Given an unsorted array of integers nums, return the length of the longest consecutive 
elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Explanation: The longest consecutive elements sequence is [0,1,2,3,4,5,6,7,8]. Therefore its length is 9.

Constraints:
- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
"""

from typing import List, Set, Tuple


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        HashSet approach with optimized sequence checking.
        Time complexity: O(n)
        Space complexity: O(n)
        """
        if not nums:
            return 0

        num_set = set(nums)
        max_length = 0

        for num in num_set:
            # Only check sequences from their smallest number
            if num - 1 not in num_set:
                current_num = num
                current_length = 1

                # Count consecutive numbers
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1

                max_length = max(max_length, current_length)

        return max_length

    def longestConsecutiveWithSequence(self, nums: List[int]) -> Tuple[int, List[int]]:
        """
        Returns both length and the actual sequence.
        Time complexity: O(n)
        Space complexity: O(n)
        """
        if not nums:
            return 0, []

        num_set = set(nums)
        max_length = 0
        max_sequence = []

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_sequence = [num]

                while current_num + 1 in num_set:
                    current_num += 1
                    current_sequence.append(current_num)

                if len(current_sequence) > max_length:
                    max_length = len(current_sequence)
                    max_sequence = current_sequence

        return max_length, max_sequence

    def longestConsecutiveUnionFind(self, nums: List[int]) -> int:
        """
        Union-Find approach.
        Time complexity: O(n)
        Space complexity: O(n)
        """
        if not nums:
            return 0

        # Initialize parent and rank dictionaries
        parent = {num: num for num in nums}
        rank = {num: 0 for num in nums}

        def find(x: int) -> int:
            """Find with path compression"""
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: int, y: int) -> None:
            """Union by rank"""
            px, py = find(x), find(y)
            if px == py:
                return
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1

        # Union consecutive numbers
        num_set = set(nums)
        for num in num_set:
            if num + 1 in num_set:
                union(num, num + 1)

        # Count sequence lengths
        sequences = {}
        for num in num_set:
            root = find(num)
            sequences[root] = sequences.get(root, 0) + 1

        return max(sequences.values()) if sequences else 0


def visualize_sequence(sequence: List[int]) -> None:
    """
    Helper function to visualize the consecutive sequence.
    """
    if not sequence:
        print("No sequence found.")
        return

    print("\nSequence visualization:")
    print("Index:", " ".join(f"{i:3}" for i in range(len(sequence))))
    print("Value:", " ".join(f"{x:3}" for x in sequence))
    print("Steps:", " ".join("→→→" if i < len(sequence)-1 else "   "
                             for i in range(len(sequence))))


def test_longest_consecutive():
    """
    Test function with various test cases.
    """
    test_cases = [
        {
            "nums": [100, 4, 200, 1, 3, 2],
            "expected": 4,
            "description": "Basic case with gaps"
        },
        {
            "nums": [0, 3, 7, 2, 5, 8, 4, 6, 0, 1],
            "expected": 9,
            "description": "Longer sequence with duplicate"
        },
        {
            "nums": [],
            "expected": 0,
            "description": "Empty array"
        },
        {
            "nums": [1],
            "expected": 1,
            "description": "Single element"
        },
        {
            "nums": [1, 2, 0, 1],
            "expected": 3,
            "description": "Sequence with duplicates"
        }
    ]

    solution = Solution()

    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{'='*80}")
        print(f"Test Case {i}: {test_case['description']}")
        print(f"Input array: {test_case['nums']}")

        # Test all implementations
        result1 = solution.longestConsecutive(test_case['nums'])
        result2, sequence = solution.longestConsecutiveWithSequence(
            test_case['nums'])
        result3 = solution.longestConsecutiveUnionFind(test_case['nums'])

        print(f"\nResults:")
        print(f"HashSet approach length: {result1}")
        print(f"Sequence tracking length: {result2}")
        print(f"Union-Find approach length: {result3}")

        if sequence:
            print(f"Longest consecutive sequence: {sequence}")
            visualize_sequence(sequence)

        assert result1 == test_case['expected'], \
            f"HashSet approach failed. Expected {test_case['expected']}, got {result1}"
        assert result2 == test_case['expected'], \
            f"Sequence tracking failed. Expected {test_case['expected']}, got {result2}"
        assert result3 == test_case['expected'], \
            f"Union-Find approach failed. Expected {test_case['expected']}, got {result3}"

        print("✓ Test case passed!")

    print("\nAll test cases passed! 🎉")


if __name__ == "__main__":
    test_longest_consecutive()
