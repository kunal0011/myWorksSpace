class Solution:
    def wateringPlants(self, plants: list[int], capacity: int) -> int:
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
