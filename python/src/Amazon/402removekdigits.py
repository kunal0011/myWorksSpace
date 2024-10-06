class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        # Iterate through the digits in num
        for digit in num:
            # Remove digits from the stack if they are greater than the current digit
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1

            # Push the current digit onto the stack
            stack.append(digit)

        # If we still have digits to remove, remove from the end
        while k > 0:
            stack.pop()
            k -= 1

        # Join the stack to form the result and remove leading zeros
        result = ''.join(stack).lstrip('0')

        # Return '0' if the result is empty
        return result if result else "0"
