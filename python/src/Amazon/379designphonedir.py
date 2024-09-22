from collections import deque


class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        """
        Initialize the PhoneDirectory with a queue of available numbers
        and a set to track which numbers are currently available.
        """
        self.available_numbers = deque(range(maxNumbers))
        self.in_use = set()

    def get(self) -> int:
        """
        Provide an available number. If none are available, return -1.
        """
        if self.available_numbers:
            number = self.available_numbers.popleft()
            self.in_use.add(number)
            return number
        return -1

    def check(self, number: int) -> bool:
        """
        Check if a number is available.
        """
        return number not in self.in_use

    def release(self, number: int) -> None:
        """
        Release a number, making it available again.
        """
        if number in self.in_use:
            self.in_use.remove(number)
            self.available_numbers.append(number)


# Test cases
if __name__ == "__main__":
    phoneDirectory = PhoneDirectory(3)
    print(phoneDirectory.get())    # It returns 0
    print(phoneDirectory.get())    # It returns 1
    print(phoneDirectory.check(2))  # It returns True, as 2 is available
    print(phoneDirectory.get())    # It returns 2
    print(phoneDirectory.check(2))  # It returns False, as 2 is not available
    phoneDirectory.release(2)
    print(phoneDirectory.check(2))  # It returns True, as 2 is available again
