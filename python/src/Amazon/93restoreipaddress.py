
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def is_valid(segment):
            # Check if the segment is valid: 0 <= int(segment) <= 255 and no leading zeros
            return int(segment) <= 255 and (segment == "0" or segment[0] != "0")

        def backtrack(start=0, dots=3, path=[]):
            # If no more dots to place
            if dots == 0:
                segment = s[start:]
                if is_valid(segment):
                    result.append(".".join(path + [segment]))
                return

            # Try placing a dot in all valid positions
            for end in range(start + 1, min(start + 4, len(s))):
                segment = s[start:end]
                if is_valid(segment):
                    backtrack(end, dots - 1, path + [segment])

        result = []
        # If the length of the string is not suitable for a valid IP address
        if not (4 <= len(s) <= 12):
            return result

        backtrack()
        return result
