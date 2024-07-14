class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        op = '+'
        n = len(s)

        for i in range(n):
            if s[i].isdigit():
                num = num * 10 + int(s[i])

            if (not s[i].isdigit() and s[i] != ' ') or i == n - 1:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop() * num)
                elif op == '/':
                    stack.append(int(stack.pop() / num))

                op = s[i]
                num = 0

        return sum(stack)
