class Solution:
    def canWin(self, s: str) -> bool:
        def canWinHelper(s):
            for i in range(len(s) - 1):
                if s[i:i+2] == '++':
                    # Try flipping and recurse
                    if not canWinHelper(s[:i] + '--' + s[i+2:]):
                        return True
            return False

        return canWinHelper(s)
