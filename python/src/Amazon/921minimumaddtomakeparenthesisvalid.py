class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # Track balance for open parentheses and unmatched closing parentheses
        balance = 0
        unmatched_closing = 0

        # Iterate through each character in the string
        for char in s:
            if char == '(':
                balance += 1  # Increase balance for an open parenthesis
            elif char == ')':
                if balance > 0:
                    balance -= 1  # Pair it with an open parenthesis
                else:
                    unmatched_closing += 1  # No matching open parenthesis, so we need to add one

        # Total number of additions needed = unmatched closing + unbalanced opening
        return unmatched_closing + balance
