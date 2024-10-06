from collections import deque


class Solution:
    def longestSubarray(self, nums, limit):
        max_deque = deque()  # To keep track of maximum elements in the window
        min_deque = deque()  # To keep track of minimum elements in the window
        left = 0  # Left pointer for the sliding window
        result = 0

        for right in range(len(nums)):
            # Maintain the decreasing order in max_deque
            while max_deque and nums[max_deque[-1]] <= nums[right]:
                max_deque.pop()
            max_deque.append(right)

            # Maintain the increasing order in min_deque
            while min_deque and nums[min_deque[-1]] >= nums[right]:
                min_deque.pop()
            min_deque.append(right)

            # If the current window violates the limit, shrink it
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                left += 1
                # Remove elements that are out of the current window from both deques
                if max_deque[0] < left:
                    max_deque.popleft()
                if min_deque[0] < left:
                    min_deque.popleft()

            # Calculate the maximum length of the valid subarray
            result = max(result, right - left + 1)

        return result

# Test cases


def test_longest_subarray():
    solution = Solution()

    # Test case 1
    nums = [8, 2, 4, 7]
    limit = 4
    assert solution.longestSubarray(nums, limit) == 2, "Test case 1 failed"

    # Test case 2
    nums = [10, 1, 2, 4, 7, 2]
    limit = 5
    assert solution.longestSubarray(nums, limit) == 4, "Test case 2 failed"

    # Test case 3
    nums = [4, 2, 2, 2, 4, 4, 2, 2]
    limit = 0
    assert solution.longestSubarray(nums, limit) == 3, "Test case 3 failed"

    print("All test cases passed!")


# Run the tests
test_longest_subarray()
