"""
LeetCode 494 - Target Sum

Problem Statement:
You are given an integer array nums and an integer target.
You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.
For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

Example:
Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

Time Complexity: O(n * sum) where n is length of array and sum is sum of all numbers
Space Complexity: O(sum) as we use a dictionary to store intermediate results
"""


def findTargetSumWays(nums: list[int], target: int) -> int:
    # Convert problem to subset sum
    # sum(P) - sum(N) = target
    # sum(P) + sum(N) = sum(nums)
    # 2 * sum(P) = target + sum(nums)
    # sum(P) = (target + sum(nums)) // 2

    total = sum(nums)

    # If target is not achievable
    if abs(target) > total:
        return 0
    if (target + total) % 2:
        return 0

    target = (target + total) // 2

    # dp[j] represents number of ways to make sum j
    dp = {0: 1}

    for num in nums:
        next_dp = dp.copy()
        for curr_sum in dp:
            next_dp[curr_sum +
                    num] = next_dp.get(curr_sum + num, 0) + dp[curr_sum]
        dp = next_dp

    return dp.get(target, 0)

# Test driver


def run_tests():
    test_cases = [
        ([1, 1, 1, 1, 1], 3, 5),
        ([1], 1, 1),
        ([1, 0], 1, 2),
        ([0, 0, 0, 0, 0, 0, 0, 0, 1], 1, 256),
        ([100], -200, 0)
    ]

    for i, (nums, target, expected) in enumerate(test_cases, 1):
        result = findTargetSumWays(nums, target)
        status = "✓" if result == expected else "✗"
        print(f"Test {i}: {status}")
        print(f"Input: nums={nums}, target={target}")
        print(f"Expected: {expected}")
        print(f"Got: {result}\n")


if __name__ == "__main__":
    run_tests()
