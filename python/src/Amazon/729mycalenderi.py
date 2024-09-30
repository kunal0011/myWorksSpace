class MyCalendar:

    def __init__(self):
        # Store the bookings as a list of tuples (start, end)
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        # Check each existing booking to ensure there's no overlap
        for s, e in self.bookings:
            # An overlap occurs if the new event starts before an existing event ends
            # and ends after an existing event starts
            if start < e and end > s:
                return False

        # If no overlap, add the new booking
        self.bookings.append((start, end))
        return True


# Test the solution with some test cases
if __name__ == "__main__":
    my_calendar = MyCalendar()

    # Test case 1
    print(my_calendar.book(10, 20))  # Expected output: True (no conflict)

    # Test case 2
    # Expected output: False (overlaps with previous event)
    print(my_calendar.book(15, 25))

    # Test case 3
    # Expected output: True (no overlap with previous events)
    print(my_calendar.book(20, 30))
