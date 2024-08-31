from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)

        if len_s1 > len_s2:
            return False

        # Frequency counter for s1
        s1_count = Counter(s1)
        # Initial window counter for the first len_s1 characters of s2
        window_count = Counter(s2[:len_s1])

        if s1_count == window_count:
            return True

        # Slide the window across s2
        for i in range(len_s1, len_s2):
            # Include a new character to the window
            window_count[s2[i]] += 1
            # Remove the leftmost character from the window
            left_char = s2[i - len_s1]
            window_count[left_char] -= 1
            # Remove the character count from the window if it becomes zero
            if window_count[left_char] == 0:
                del window_count[left_char]

            # Compare window with s1_count
            if s1_count == window_count:
                return True

        return False
