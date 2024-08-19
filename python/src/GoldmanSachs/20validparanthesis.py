class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Dictionary to hold matching pairs of parentheses
        mapping = {")": "(", "}": "{", "]": "["}

        # Iterate over each character in the string
        for char in s:
            # If the character is a closing bracket
            if char in mapping:
                # Pop the top element from the stack (if it exists)
                top_element = stack.pop() if stack else '#'

                # If the popped element doesn't match the corresponding opening bracket
                if mapping[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)

        # If the stack is empty, all opening brackets have been matched
        return not stack
