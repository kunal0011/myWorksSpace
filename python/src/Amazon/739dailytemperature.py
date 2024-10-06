class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        answer = [0] * n  # Initialize the result array with 0s
        stack = []  # Stack to store indices

        for i, temp in enumerate(temperatures):
            # While stack is not empty and current temperature is greater than
            # the temperature at the index stored at the top of the stack
            while stack and temperatures[stack[-1]] < temp:
                idx = stack.pop()
                answer[idx] = i - idx  # Calculate the number of days
            stack.append(i)  # Push current index onto the stack

        return answer
