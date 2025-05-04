"""
LeetCode 2079 - Watering Plants

Problem Statement:
You want to water n plants in your garden with a watering can. The plants are arranged in a row and are labeled 
from 0 to n - 1 from left to right where the ith plant is located at x = i. Each plant needs a specific amount 
of water. You will water the plants in the following way:
- Water the plants in order from left to right.
- After watering the current plant, if you do not have enough water to completely water the next plant, 
  you need to refill your watering can by returning to the river.
- You cannot refill the watering can early.
- You are initially at the river (i.e., x = -1). It takes one step to move one unit on the x-axis.

Time Complexity: O(n) where n is the number of plants
Space Complexity: O(1) as we only use constant extra space
"""


class Solution:
    def wateringPlants(self, plants: list[int], capacity: int) -> int:
        """
        Logic:
        1. Keep track of steps and current water capacity
        2. For each plant:
           - If we have enough water, just add 1 step and reduce capacity
           - If not enough water:
             * Need to go back to river (i steps) and return to current plant (i steps)
             * Plus 1 step for watering current plant
             * Reset capacity and reduce by current plant's need

        Args:
            plants: List of integers representing water needed by each plant
            capacity: Integer representing watering can capacity
        Returns:
            Total number of steps needed
        """
        steps = 0
        current_capacity = capacity

        for i, water_needed in enumerate(plants):
            if water_needed <= current_capacity:
                steps += 1
                current_capacity -= water_needed
            else:
                steps += 2 * i + 1
                current_capacity = capacity - water_needed

        return steps


# Test driver
def main():
    # Test cases
    test_cases = [
        {
            'plants': [2, 2, 3, 3],
            'capacity': 5,
            'expected': 14
        },
        {
            'plants': [1, 1, 1, 4, 2, 3],
            'capacity': 4,
            'expected': 30
        },
        {
            'plants': [7, 7, 7, 7, 7, 7, 7],
            'capacity': 8,
            'expected': 49
        }
    ]

    solution = Solution()

    for i, test in enumerate(test_cases, 1):
        result = solution.wateringPlants(test['plants'], test['capacity'])
        status = "PASSED" if result == test['expected'] else "FAILED"
        print(f"Test {i}: {status}")
        print(
            f"Input: plants = {test['plants']}, capacity = {test['capacity']}")
        print(f"Output: {result}")
        print(f"Expected: {test['expected']}\n")


if __name__ == "__main__":
    main()
