class Solution:
    def getMaxLen(self, nums) -> int:
        # Initialize lengths of the positive and negative product subarrays
        positive_len = 0
        negative_len = 0
        max_len = 0

        # Iterate over the array
        for num in nums:
            if num == 0:
                # Reset lengths if we encounter zero
                positive_len = 0
                negative_len = 0
            elif num > 0:
                # Increase positive_len, and increase negative_len if it's already non-zero
                positive_len += 1
                negative_len = negative_len + 1 if negative_len > 0 else 0
            else:
                # Swap positive_len and negative_len since multiplying by negative changes sign
                temp = positive_len
                positive_len = negative_len + 1 if negative_len > 0 else 0
                negative_len = temp + 1

            # Update max_len with the maximum length of the positive product subarray
            max_len = max(max_len, positive_len)

        return max_len
