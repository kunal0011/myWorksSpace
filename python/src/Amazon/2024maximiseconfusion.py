class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def maxConsecutiveChar(char: str) -> int:
            left = 0
            max_len = 0
            flips = 0

            for right in range(len(answerKey)):
                if answerKey[right] != char:
                    flips += 1

                while flips > k:
                    if answerKey[left] != char:
                        flips -= 1
                    left += 1

                max_len = max(max_len, right - left + 1)

            return max_len

        # Maximize consecutive 'T's or 'F's
        return max(maxConsecutiveChar('T'), maxConsecutiveChar('F'))


# Testing the solution
if __name__ == "__main__":
    solution = Solution()

    # Test case
    answerKey = "TTFF"
    k = 2
    print("Maximum consecutive identical answers:",
          solution.maxConsecutiveAnswers(answerKey, k))  # Expected output: 4
