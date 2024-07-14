class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def maxLengthWithCharChange(char_to_change: str) -> int:
            max_len = 0
            left = 0
            count_changes = 0

            for right in range(len(answerKey)):
                if answerKey[right] == char_to_change:
                    count_changes += 1

                while count_changes > k:
                    if answerKey[left] == char_to_change:
                        count_changes -= 1
                    left += 1

                max_len = max(max_len, right - left + 1)

            return max_len

        return max(maxLengthWithCharChange('T'), maxLengthWithCharChange('F'))


# Example usage:
sol = Solution()
answerKey1 = "TTFF"
k1 = 2
print(sol.maxConsecutiveAnswers(answerKey1, k1))  # Output: 4

answerKey2 = "TFFT"
k2 = 1
print(sol.maxConsecutiveAnswers(answerKey2, k2))  # Output: 3

answerKey3 = "TTFTTFTT"
k3 = 1
print(sol.maxConsecutiveAnswers(answerKey3, k3))  # Output: 5
