class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1:
            return encodedText

        cols = len(encodedText) // rows
        decodedText = []

        for startCol in range(cols):
            for row, col in zip(range(rows), range(startCol, cols)):
                decodedText.append(encodedText[row * cols + col])

        # Join and strip trailing spaces
        return ''.join(decodedText).rstrip()
