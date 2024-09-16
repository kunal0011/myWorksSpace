import heapq


class Solution:
    def minimumDeviation(self, nums):
        # Step 1: Make all numbers even by multiplying odd numbers by 2
        nums = [-num * 2 if num % 2 != 0 else -num for num in nums]

        # Step 2: Create a max-heap (using negative values to simulate max-heap in Python)
        heapq.heapify(nums)
        min_val = -max(nums)
        min_deviation = float('inf')

        while True:
            max_val = -heapq.heappop(nums)
            min_deviation = min(min_deviation, max_val - min_val)

            # If the max element is odd, stop the process
            if max_val % 2 == 1:
                break

            # Otherwise, divide the max element by 2 and push it back into the heap
            new_val = max_val // 2
            heapq.heappush(nums, -new_val)
            min_val = min(min_val, new_val)

        return min_deviation


# Testing
solution = Solution()
nums = [1, 2, 3, 4]
print("Python Test Result:", solution.minimumDeviation(nums))  # Output should be 1
