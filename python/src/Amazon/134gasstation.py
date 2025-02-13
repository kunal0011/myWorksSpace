"""
LeetCode 134. Gas Station

Problem Statement:
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station 
to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once in the clockwise 
direction, otherwise return -1.

Note:
- If there exists a solution, it is guaranteed to be unique
- Both input arrays are non-empty and have the same length
- Each element in the input arrays is a non-negative integer

Example 1:
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

Example 2:
Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation: You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.

Constraints:
- n == gas.length == cost.length
- 1 <= n <= 10^5
- 0 <= gas[i], cost[i] <= 10^4
"""

from typing import List, Tuple


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        One-pass solution with optimization.
        Time complexity: O(n)
        Space complexity: O(1)
        """
        if sum(gas) < sum(cost):
            return -1

        start = 0
        tank = 0

        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                # If we can't reach next station, try starting from next station
                start = i + 1
                tank = 0

        return start

    def canCompleteCircuitWithPath(self, gas: List[int], cost: List[int]) -> Tuple[int, List[int]]:
        """
        Returns both starting index and the path with gas levels.
        Time complexity: O(n)
        Space complexity: O(n) for storing path
        """
        if sum(gas) < sum(cost):
            return -1, []

        n = len(gas)
        start = 0
        tank = 0
        path = []

        # Find starting point
        for i in range(n):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0

        # Simulate journey from starting point
        tank = 0
        current = start
        for _ in range(n):
            tank += gas[current]
            path.append((current, tank))
            tank -= cost[current]
            # Update with remaining gas
            path[-1] = (current, path[-1][1], tank)
            current = (current + 1) % n

        return start, path


def visualize_journey(gas: List[int], cost: List[int], path: List[Tuple[int, int, int]]) -> None:
    """
    Helper function to visualize the journey with gas levels.
    """
    print("\nJourney visualization:")
    print("Station | Gas Available | Cost to Next | Remaining")
    print("-" * 50)

    for station, gas_level, remaining in path:
        print(
            f"{station:7d} | {gas_level:12d} | {cost[station]:11d} | {remaining:9d}")


def test_gas_station():
    """
    Test function with various test cases.
    """
    test_cases = [
        {
            "gas": [1, 2, 3, 4, 5],
            "cost": [3, 4, 5, 1, 2],
            "expected": 3,
            "description": "Standard case with solution"
        },
        {
            "gas": [2, 3, 4],
            "cost": [3, 4, 3],
            "expected": -1,
            "description": "No solution possible"
        },
        {
            "gas": [5, 1, 2, 3, 4],
            "cost": [4, 4, 1, 5, 1],
            "expected": 4,
            "description": "Solution at last station"
        },
        {
            "gas": [1, 2, 3, 4, 5],
            "cost": [1, 2, 3, 4, 5],
            "expected": 0,
            "description": "Equal gas and cost"
        },
        {
            "gas": [2],
            "cost": [2],
            "expected": 0,
            "description": "Single station"
        }
    ]

    solution = Solution()

    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{'='*80}")
        print(f"Test Case {i}: {test_case['description']}")
        print(f"Gas stations: {test_case['gas']}")
        print(f"Travel costs: {test_case['cost']}")

        # Test both implementations
        result1 = solution.canCompleteCircuit(
            test_case['gas'], test_case['cost'])
        result2, path = solution.canCompleteCircuitWithPath(
            test_case['gas'], test_case['cost'])

        print(f"\nResults:")
        print(f"Starting station: {result1}")

        if result1 != -1:
            print(f"Total gas available: {sum(test_case['gas'])}")
            print(f"Total cost needed: {sum(test_case['cost'])}")
            visualize_journey(test_case['gas'], test_case['cost'], path)
        else:
            print("No valid solution exists.")

        assert result1 == test_case['expected'], \
            f"Basic approach failed. Expected {test_case['expected']}, got {result1}"
        assert result2 == test_case['expected'], \
            f"Path tracking failed. Expected {test_case['expected']}, got {result2}"

        print("✓ Test case passed!")

    print("\nAll test cases passed! 🎉")


if __name__ == "__main__":
    test_gas_station()
