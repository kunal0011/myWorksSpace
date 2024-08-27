class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # First pass to remove invalid closing parentheses
        stack = []
        to_remove = set()

        # Identify unmatched closing parentheses
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    to_remove.add(i)

        # Add remaining unmatched opening parentheses to removal set
        to_remove.update(stack)

        # Build result string excluding characters in removal set
        return ''.join(char for i, char in enumerate(s) if i not in to_remove)
