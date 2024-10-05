class Solution:
    def reverseString(self, s: list) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        # Use two pointers: one starting from the left, the other from the right
        while left < right:
            # Swap the characters
            s[left], s[right] = s[right], s[left]
            # Move towards the center
            left += 1
            right -= 1
