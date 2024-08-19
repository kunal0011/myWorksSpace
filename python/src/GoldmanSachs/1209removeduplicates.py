class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  # Stack to keep track of characters and their counts

        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
                # If the count of the current character reaches k, pop it from the stack
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char, 1])

        # Build the result string from the stack
        result = ''.join(char * count for char, count in stack)
        return result
