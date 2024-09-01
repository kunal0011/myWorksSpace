class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # Strategy: Remove substrings greedily
        # Process higher point substring first to maximize the score

        def remove_pair(s, first, second, points):
            stack = []
            score = 0
            for char in s:
                if stack and stack[-1] == first and char == second:
                    stack.pop()
                    score += points
                else:
                    stack.append(char)
            return score, ''.join(stack)

        if x >= y:
            score1, leftover = remove_pair(s, 'a', 'b', x)
            score2, _ = remove_pair(leftover, 'b', 'a', y)
        else:
            score1, leftover = remove_pair(s, 'b', 'a', y)
            score2, _ = remove_pair(leftover, 'a', 'b', x)

        return score1 + score2
