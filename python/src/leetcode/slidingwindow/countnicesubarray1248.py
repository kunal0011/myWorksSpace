class Solution:

    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        # This will store the count of subarrays with a certain number of odd numbers
        count = {0: 1}
        current_odd_count = 0
        result = 0

        for num in nums:
            # Increment the odd count if the current number is odd
            if num % 2 == 1:
                current_odd_count += 1

            # If there are `current_odd_count - k` subarrays that end before the current index
            # with exactly `current_odd_count - k` odd numbers, then there are that many subarrays
            # ending at the current index with exactly `k` odd numbers
            if current_odd_count - k in count:
                result += count[current_odd_count - k]

            # Update the count of subarrays with `current_odd_count` odd numbers
            if current_odd_count in count:
                count[current_odd_count] += 1
            else:
                count[current_odd_count] = 1

        return result


# Example usage:
sol = Solution()
nums1 = [1, 1, 2, 1, 1]
k1 = 3
print(sol.numberOfSubarrays(nums1, k1))  # Output: 2

nums2 = [2, 4, 6]
k2 = 1
print(sol.numberOfSubarrays(nums2, k2))  # Output: 0

nums3 = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2]
k3 = 2
print(sol.numberOfSubarrays(nums3, k3))  # Output: 16
