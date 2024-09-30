import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # Step 1: Convert the stones list into a max-heap by pushing negative values
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        # Step 2: Smash stones until one or zero stones remain
        while len(max_heap) > 1:
            # Extract the two largest stones (remember they are negative, so smallest values)
            first = -heapq.heappop(max_heap)  # Get the largest
            second = -heapq.heappop(max_heap)  # Get the second largest

            # Step 3: If they are not the same, push the difference back into the heap
            if first != second:
                heapq.heappush(max_heap, -(first - second))

        # Step 4: If no stones left, return 0, otherwise return the remaining stone (negated)
        return -max_heap[0] if max_heap else 0

# Testing the implementation


def test_last_stone_weight():
    solution = Solution()

    # Test case 1
    stones1 = [2, 7, 4, 1, 8, 1]
    # Expected output: 1 (Explanation: The last stone weight after all smashes is 1)
    result1 = solution.lastStoneWeight(stones1)
    print(f"Test 1 - Result: {result1}, Expected: 1")

    # Test case 2
    stones2 = [1]
    # Expected output: 1 (Only one stone, so it remains as is)
    result2 = solution.lastStoneWeight(stones2)
    print(f"Test 2 - Result: {result2}, Expected: 1")

    # Test case 3
    stones3 = [3, 3, 3, 3]
    # Expected output: 0 (All stones destroy each other)
    result3 = solution.lastStoneWeight(stones3)
    print(f"Test 3 - Result: {result3}, Expected: 0")


# Run the test
test_last_stone_weight()
