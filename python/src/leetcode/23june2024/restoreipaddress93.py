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


def restoreIpAddresses(s):
    def is_valid(segment):
        # Check if the segment is valid: 0 <= int(segment) <= 255 and no leading zeros
        return 0 <= int(segment) <= 255 and (segment == "0" or segment[0] != "0")

    result = []
    n = len(s)

    # Iterate over possible positions for the first dot
    for i in range(1, min(n, 4)):
        first = s[:i]
        if not is_valid(first):
            continue

        # Iterate over possible positions for the second dot
        for j in range(i + 1, min(n, i + 4)):
            second = s[i:j]
            if not is_valid(second):
                continue

            # Iterate over possible positions for the third dot
            for k in range(j + 1, min(n, j + 4)):
                third = s[j:k]
                fourth = s[k:]

                if is_valid(third) and is_valid(fourth):
                    result.append(".".join([first, second, third, fourth]))

    return result


# Example usage
s = "25525511135"
s1 = Solution()
print(s1.restoreIpAddresses(s))  # Output: ["255.255.11.135","255.255.111.35"]
