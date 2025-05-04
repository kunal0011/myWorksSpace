"""
LeetCode 667 - Beautiful Arrangement II

Problem Statement:
Given two integers n and k, construct an array of n integers such that:
1. All integers from 1 to n are used exactly once
2. The array contains exactly k different absolute differences between adjacent elements
3. Return any valid array that satisfies the conditions

Logic:
1. Key insight: To create k different absolute differences with minimum numbers:
   - Place numbers alternatively from both ends of range [1,n]
   - This creates differences: k, k-1, k-2, ..., 1
2. Solution approach:
   - First k+1 elements: alternate between smallest and largest available numbers
   - Remaining elements: append sequentially
3. Example for n=6, k=3:
   - [1,4,2,3,5,6] creates differences [3,2,1,2,1]

Time Complexity: O(n)
Space Complexity: O(1) excluding output array
"""


class Solution:
    def constructArray(self, n: int, k: int) -> list[int]:
        result = []

        # First, create the first k+1 elements to have k distinct differences
        for i in range(1, k+2):
            if i % 2 != 0:  # Odd index, pick from the start
                result.append((i + 1) // 2)
            else:  # Even index, pick from the end
                result.append(k + 2 - i // 2)

        # Then fill the rest of the numbers sequentially
        for i in range(k + 2, n + 1):
            result.append(i)

        return result


def get_differences(arr):
    """Helper function to get absolute differences between adjacent elements"""
    return [abs(arr[i] - arr[i-1]) for i in range(1, len(arr))]


def test_beautiful_arrangement():
    solution = Solution()

    test_cases = [
        {
            'n': 3,
            'k': 1,
            'description': "Minimum possible differences"
        },
        {
            'n': 6,
            'k': 3,
            'description': "Medium case"
        },
        {
            'n': 5,
            'k': 4,
            'description': "Maximum possible differences"
        },
        {
            'n': 10,
            'k': 4,
            'description': "Larger n with smaller k"
        }
    ]

    print("Testing Beautiful Arrangement II Solution:")
    for i, test in enumerate(test_cases, 1):
        n, k = test['n'], test['k']
        result = solution.constructArray(n, k)
        differences = get_differences(result)
        unique_differences = len(set(differences))

        print(f"\nTest Case {i} ({test['description']}):")
        print(f"Input: n={n}, k={k}")
        print(f"Generated array: {result}")
        print(f"Adjacent differences: {differences}")
        print(f"Number of unique differences: {unique_differences}")
        print(f"Status: {'PASSED' if unique_differences == k else 'FAILED'}")

        # Verify all numbers 1 to n are used
        used_all = sorted(result) == list(range(1, n + 1))
        print(f"Used all numbers 1 to {n}: {'Yes' if used_all else 'No'}")


if __name__ == "__main__":
    test_beautiful_arrangement()
