"""
LeetCode 164. Maximum Gap

Problem Statement:
Given an integer array nums, return the maximum difference between two successive elements 
in its sorted form. If the array contains less than 2 elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra space.

Example 1:
Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.

Example 2:
Input: nums = [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^9
"""

from typing import List, Tuple
from math import ceil


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        """
        Bucket sort approach.
        Time complexity: O(n)
        Space complexity: O(n)
        """
        if len(nums) < 2:
            return 0

        # Find min and max values
        min_val, max_val = min(nums), max(nums)
        if min_val == max_val:
            return 0

        # Calculate bucket size and number of buckets
        n = len(nums)
        bucket_size = ceil((max_val - min_val) / (n - 1))
        if bucket_size == 0:
            bucket_size = 1

        # Initialize buckets with None values
        buckets = [(float('inf'), float('-inf'))
                   for _ in range((max_val - min_val) // bucket_size + 1)]

        # Fill buckets with min and max values
        for num in nums:
            idx = (num - min_val) // bucket_size
            buckets[idx] = (min(buckets[idx][0], num),
                            max(buckets[idx][1], num))

        # Find maximum gap between buckets
        max_gap = 0
        prev_max = min_val

        for bucket_min, bucket_max in buckets:
            if bucket_min == float('inf'):  # Empty bucket
                continue
            max_gap = max(max_gap, bucket_min - prev_max)
            prev_max = bucket_max

        return max_gap

    def maximumGapWithSteps(self, nums: List[int]) -> Tuple[int, List[dict]]:
        """
        Returns maximum gap and intermediate steps.
        Time complexity: O(n)
        Space complexity: O(n)
        """
        steps = []

        if len(nums) < 2:
            steps.append({
                "action": "Early return",
                "reason": "Less than 2 elements",
                "result": 0
            })
            return 0, steps

        # Find min and max values
        min_val, max_val = min(nums), max(nums)
        steps.append({
            "action": "Find range",
            "min_val": min_val,
            "max_val": max_val
        })

        if min_val == max_val:
            steps.append({
                "action": "Early return",
                "reason": "All elements equal",
                "result": 0
            })
            return 0, steps

        # Calculate bucket parameters
        n = len(nums)
        bucket_size = ceil((max_val - min_val) / (n - 1))
        if bucket_size == 0:
            bucket_size = 1
        num_buckets = (max_val - min_val) // bucket_size + 1

        steps.append({
            "action": "Calculate buckets",
            "bucket_size": bucket_size,
            "num_buckets": num_buckets
        })

        # Initialize buckets
        buckets = [(float('inf'), float('-inf')) for _ in range(num_buckets)]

        # Fill buckets
        for num in nums:
            idx = (num - min_val) // bucket_size
            old_min, old_max = buckets[idx]
            buckets[idx] = (min(old_min, num), max(old_max, num))

        steps.append({
            "action": "Fill buckets",
            "buckets": [(min_val, max_val) if min_val != float('inf') else None
                        for min_val, max_val in buckets]
        })

        # Find maximum gap
        max_gap = 0
        prev_max = min_val
        gaps = []

        for bucket_min, bucket_max in buckets:
            if bucket_min == float('inf'):  # Empty bucket
                continue
            gap = bucket_min - prev_max
            gaps.append(gap)
            max_gap = max(max_gap, gap)
            prev_max = bucket_max

        steps.append({
            "action": "Find gaps",
            "gaps": gaps,
            "max_gap": max_gap
        })

        return max_gap, steps


def visualize_steps(nums: List[int], steps: List[dict]) -> None:
    """Helper function to visualize algorithm steps."""
    print("\nAlgorithm Steps:")
    for i, step in enumerate(steps, 1):
        print(f"\nStep {i}: {step['action']}")

        if step['action'] == "Early return":
            print(f"Reason: {step['reason']}")
            print(f"Result: {step['result']}")

        elif step['action'] == "Find range":
            print(f"Min value: {step['min_val']}")
            print(f"Max value: {step['max_val']}")

        elif step['action'] == "Calculate buckets":
            print(f"Bucket size: {step['bucket_size']}")
            print(f"Number of buckets: {step['num_buckets']}")

        elif step['action'] == "Fill buckets":
            print("Bucket contents:")
            for j, bucket in enumerate(step['buckets']):
                if bucket:
                    print(f"Bucket {j}: {bucket}")

        elif step['action'] == "Find gaps":
            print("Gaps between buckets:", step['gaps'])
            print(f"Maximum gap: {step['max_gap']}")


def test_maximum_gap():
    """
    Test function with various test cases.
    """
    test_cases = [
        {
            "nums": [3, 6, 9, 1],
            "expected": 3,
            "description": "Basic case"
        },
        {
            "nums": [10],
            "expected": 0,
            "description": "Single element"
        },
        {
            "nums": [1, 1, 1, 1],
            "expected": 0,
            "description": "All equal elements"
        },
        {
            "nums": [1, 10000000],
            "expected": 9999999,
            "description": "Large gap"
        },
        {
            "nums": [1, 2, 3, 4, 5],
            "expected": 1,
            "description": "Consecutive numbers"
        }
    ]

    solution = Solution()

    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{'='*80}")
        print(f"Test Case {i}: {test_case['description']}")
        print(f"Input array: {test_case['nums']}")

        # Test both implementations
        result1 = solution.maximumGap(test_case['nums'])
        result2, steps = solution.maximumGapWithSteps(test_case['nums'])

        print(f"\nResults:")
        print(f"Maximum gap: {result1}")

        visualize_steps(test_case['nums'], steps)

        assert result1 == test_case['expected'], \
            f"Basic approach failed. Expected {test_case['expected']}, got {result1}"
        assert result2 == test_case['expected'], \
            f"Step tracking failed. Expected {test_case['expected']}, got {result2}"

        print("✓ Test case passed!")

    print("\nAll test cases passed! 🎉")


if __name__ == "__main__":
    test_maximum_gap()
