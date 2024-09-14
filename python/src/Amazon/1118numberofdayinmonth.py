class Solution:
    def numberOfDays(self, Y: int, M: int) -> int:
        # Check if it's February
        if M == 2:
            # Leap year check
            if (Y % 4 == 0 and Y % 100 != 0) or (Y % 400 == 0):
                return 29
            else:
                return 28
        # Months with 31 days
        elif M in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        # Months with 30 days
        else:
            return 30
