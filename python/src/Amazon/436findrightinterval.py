import bisect


class Solution:
    def findRightInterval(self, intervals: list[list[int]]) -> list[int]:
        # Step 1: Create a list of (start, index) tuples
        starts = sorted((interval[0], i)
                        for i, interval in enumerate(intervals))

        # Step 2: Result array
        res = []

        # Step 3: For each interval, find the right interval using binary search
        for interval in intervals:
            end = interval[1]
            # Perform binary search to find the smallest start >= end
            idx = bisect.bisect_left(starts, (end,))
            if idx < len(starts):
                res.append(starts[idx][1])
            else:
                res.append(-1)

        return res


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    intervals1 = [[1, 2]]
    print(sol.findRightInterval(intervals1))  # Expected output: [-1]

    # Test case 2
    intervals2 = [[3, 4], [2, 3], [1, 2]]
    print(sol.findRightInterval(intervals2))  # Expected output: [-1, 0, 1]

    # Test case 3
    intervals3 = [[1, 4], [2, 3], [3, 4]]
    print(sol.findRightInterval(intervals3))  # Expected output: [-1, 2, -1]
