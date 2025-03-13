"""
LeetCode 729: My Calendar I

Implement a MyCalendar class to store your events. A new event can be added if adding 
the event will not cause a double booking.

Your class will have the method book(int start, int end). Formally, this represents a 
booking on the half open interval [start, end), the range of real numbers x such that 
start <= x < end.

A double booking happens when two events have some non-empty intersection (ie., there is 
some time that is common to both events.)

Time Complexity:
- Initialization: O(1)
- Booking: O(log n) using binary search, where n is the number of existing bookings
Space Complexity: O(n) where n is the number of successful bookings
"""

from bisect import bisect_left

class MyCalendar:
    def __init__(self):
        self.bookings = []  # Store bookings in sorted order by start time

    def book(self, start: int, end: int) -> bool:
        # Use binary search to find the position where the new booking should go
        pos = bisect_left(self.bookings, (start, end))
        
        # Check for overlap with previous booking
        if pos > 0 and self.bookings[pos-1][1] > start:
            return False
            
        # Check for overlap with next booking
        if pos < len(self.bookings) and self.bookings[pos][0] < end:
            return False
            
        self.bookings.insert(pos, (start, end))
        return True

def test_my_calendar():
    """Comprehensive test driver for MyCalendar class"""
    calendar = MyCalendar()
    
    # Test cases with expected results
    test_cases = [
        ((10, 20), True, "Non-overlapping booking"),
        ((15, 25), False, "Overlapping booking in the middle"),
        ((20, 30), True, "Back-to-back booking"),
        ((5, 10), True, "Non-overlapping booking before all events"),
        ((30, 40), True, "Non-overlapping booking after all events"),
        ((25, 35), False, "Overlapping with existing booking"),
        ((5, 15), False, "Overlapping with start of existing booking"),
        ((15, 35), False, "Overlapping multiple bookings"),
    ]
    
    # Run all test cases
    for i, ((start, end), expected, description) in enumerate(test_cases, 1):
        result = calendar.book(start, end)
        status = "✓" if result == expected else "✗"
        print(f"Test {i}: {status} [{start}, {end}] -> {result} ({description})")
        if result != expected:
            print(f"  Expected: {expected}")

if __name__ == "__main__":
    test_my_calendar()
