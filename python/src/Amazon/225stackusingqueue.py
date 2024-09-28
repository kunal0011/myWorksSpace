from collections import deque


class MyStack:
    def __init__(self):
        self.q1 = deque()  # Primary queue for push
        self.q2 = deque()  # Temporary queue for pop

    def push(self, x: int) -> None:
        # Push element to q1
        self.q1.append(x)

    def pop(self) -> int:
        # Move elements from q1 to q2 until only one element is left in q1
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())

        # The last remaining element is the "top" of the stack
        result = self.q1.popleft()

        # Swap the names of q1 and q2
        self.q1, self.q2 = self.q2, self.q1
        return result

    def top(self) -> int:
        # Move elements from q1 to q2 until only one element is left in q1
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())

        # The last element is the "top" of the stack
        result = self.q1.popleft()
        self.q2.append(result)  # Put the last element into q2

        # Swap the names of q1 and q2
        self.q1, self.q2 = self.q2, self.q1
        return result

    def empty(self) -> bool:
        # If q1 is empty, the stack is empty
        return not self.q1
