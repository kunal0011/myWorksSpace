class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        max_count = 0
        count = {}
        left = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_count = max(max_count, count[s[right]])

            # If the current window size minus the most frequent character's count is greater than k,
            # it means we need more than k replacements, so we shrink the window
            if (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1

            # Calculate the maximum length of valid window
            max_len = max(max_len, right - left + 1)

        return max_len
