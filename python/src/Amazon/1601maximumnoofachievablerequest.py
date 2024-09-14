class Solution:
    def maximumRequests(self, n: int, requests: list[list[int]]) -> int:
        self.max_requests = 0
        net_change = [0] * n
        self.backtrack(requests, net_change, 0, 0)
        return self.max_requests

    def backtrack(self, requests, net_change, index, count):
        if index == len(requests):
            # Check if all buildings have balanced net change
            if all(x == 0 for x in net_change):
                self.max_requests = max(self.max_requests, count)
            return

        # Option 1: Include the current request
        from_bldg, to_bldg = requests[index]
        net_change[from_bldg] -= 1  # Someone leaves the 'from' building
        net_change[to_bldg] += 1    # Someone enters the 'to' building
        self.backtrack(requests, net_change, index + 1, count + 1)

        # Backtrack: Undo the changes
        net_change[from_bldg] += 1
        net_change[to_bldg] -= 1

        # Option 2: Exclude the current request
        self.backtrack(requests, net_change, index + 1, count)
