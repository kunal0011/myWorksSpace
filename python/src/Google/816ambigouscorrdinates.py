class Solution:
    def ambiguousCoordinates(self, s: str) -> list[str]:
        def get_valid_numbers(s: str) -> list[str]:
            n = len(s)
            results = []
            # Check if s can be a valid integer without decimal
            if s == "0" or s[0] != '0':
                results.append(s)
            # Check if s can be a valid float with decimal
            for i in range(1, n):
                left, right = s[:i], s[i:]
                if (left == "0" or left[0] != '0') and right[-1] != '0':
                    results.append(left + "." + right)
            return results

        s = s[1:-1]  # Strip out the outer parentheses
        n = len(s)
        result = []

        # Split s into two parts, left and right
        for i in range(1, n):
            left_candidates = get_valid_numbers(s[:i])
            right_candidates = get_valid_numbers(s[i:])
            # Combine valid left and right pairs
            for left in left_candidates:
                for right in right_candidates:
                    result.append(f"({left}, {right})")

        return result
