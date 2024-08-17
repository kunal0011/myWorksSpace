class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_num = 0
        current_string = ""

        for char in s:
            if char.isdigit():
                # Build the current number
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # Push the current string and current number onto the stack
                stack.append((current_string, current_num))
                # Reset current string and number
                current_string = ""
                current_num = 0
            elif char == ']':
                # Pop from stack and repeat the current string
                last_string, num = stack.pop()
                current_string = last_string + num * current_string
            else:
                # Accumulate the characters in current_string
                current_string += char

        return current_string
