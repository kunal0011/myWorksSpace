class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_number = 0
        current_result = 0
        sign = 1  # 1 for positive, -1 for negative
        result = 0

        i = 0
        while i < len(s):
            char = s[i]

            if char.isdigit():
                current_number = 0
                while i < len(s) and s[i].isdigit():
                    current_number = current_number * 10 + int(s[i])
                    i += 1
                result += sign * current_number
                continue  # to skip the increment in the for loop

            elif char == '+':
                sign = 1
            elif char == '-':
                sign = -1
            elif char == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char == ')':
                result = stack.pop() * result + stack.pop()

            i += 1

        return result
