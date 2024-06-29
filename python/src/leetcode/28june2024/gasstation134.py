from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        net_gas = [gas[i] - cost[i] for i in range(n)]

        if sum(net_gas) < 0:
            return -1

        start = 0
        current_tank = 0

        for i in range(n):
            current_tank += net_gas[i]
            if current_tank < 0:
                start = i + 1
                current_tank = 0

        return start if start < n else -1
