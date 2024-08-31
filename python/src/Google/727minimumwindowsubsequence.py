from collections import Counter, defaultdict


class Solution:
    def minWindow(self, S: str, T: str) -> str:
        # Step 1: Initialize the character counts
        t_count = Counter(T)
        s_count = defaultdict(int)

        # Step 2: Initialize pointers and variables
        min_len = float('inf')
        min_window = ""
        left = 0
        required = len(t_count)
        formed = 0

        # Step 3: Start sliding window
        for right in range(len(S)):
            char = S[right]
            s_count[char] += 1

            if char in t_count and s_count[char] == t_count[char]:
                formed += 1

            while left <= right and formed == required:
                char = S[left]

                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_window = S[left:right + 1]

                s_count[char] -= 1
                if char in t_count and s_count[char] < t_count[char]:
                    formed -= 1

                left += 1

        return min_window if min_len != float('inf') else ""


# Example usage
solution = Solution()
S1 = "abcdebdde"
T1 = "bde"

S2 = "abdabca"
T2 = "abc"

print(solution.minWindow(S1, T1))  # Output: "bcde"
print(solution.minWindow(S2, T2))  # Output: "abc"
