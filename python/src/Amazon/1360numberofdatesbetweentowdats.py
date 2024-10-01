from datetime import datetime


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        # Step 1: Convert the date strings to datetime objects
        d1 = datetime.strptime(date1, "%Y-%m-%d")
        d2 = datetime.strptime(date2, "%Y-%m-%d")

        # Step 2: Calculate the difference in days and return the absolute value
        return abs((d2 - d1).days)

# Test cases


def test_daysBetweenDates():
    sol = Solution()

    # Test Case 1: Typical case with two different dates
    assert sol.daysBetweenDates(
        "2020-01-15", "2019-12-31") == 15, "Test Case 1 Failed"

    # Test Case 2: Same day comparison
    assert sol.daysBetweenDates(
        "2020-01-01", "2020-01-01") == 0, "Test Case 2 Failed"

    # Test Case 3: Leap year case
    assert sol.daysBetweenDates(
        "2020-02-28", "2020-03-01") == 2, "Test Case 3 Failed"

    # Test Case 4: Different years
    assert sol.daysBetweenDates(
        "2020-12-31", "2019-01-01") == 730, "Test Case 4 Failed"

    print("All test cases passed!")


# Run the tests
test_daysBetweenDates()
