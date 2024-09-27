from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1, len_s2 = len(s1), len(s2)

        if len_s1 > len_s2:
            return False

        # Frequency counter for s1
        s1_count = Counter(s1)
        # Initial window frequency counter
        window_count = Counter(s2[:len_s1])

        # Check the first window
        if s1_count == window_count:
            return True

        # Sliding window to compare counts of each window
        for i in range(len_s1, len_s2):
            # Add the next character in the window
            window_count[s2[i]] += 1
            # Remove the character that is no longer in the window
            window_count[s2[i - len_s1]] -= 1

            # Remove the count completely if it's zero to match Counter's behavior
            if window_count[s2[i - len_s1]] == 0:
                del window_count[s2[i - len_s1]]

            # Check if the window matches s1's character count
            if s1_count == window_count:
                return True

        return False
