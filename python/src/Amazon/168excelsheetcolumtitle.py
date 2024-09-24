class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []

        while columnNumber > 0:
            # Adjust columnNumber to be 0-indexed
            columnNumber -= 1

            # Find the corresponding letter and append to result
            remainder = columnNumber % 26
            result.append(chr(remainder + ord('A')))

            # Update columnNumber for the next iteration
            columnNumber //= 26

        # Reverse the result list and join to form the final string
        return ''.join(reversed(result))
