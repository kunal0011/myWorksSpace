class Solution:
    def findPermutation(self, s: str):
        n = len(s) + 1
        result = []
        stack = []

        for i in range(1, n + 1):
            stack.append(i)  # Push the current number to the stack

            # If we reach an 'I' or the end of the string, pop all elements in the stack
            if i == n or s[i - 1] == 'I':
                while stack:
                    result.append(stack.pop())

        return result
