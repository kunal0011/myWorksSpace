class StockSpanner:
    def __init__(self):
        # Stack to store pairs of (price, span)
        self.stack = []

    def next(self, price: int) -> int:
        # Initialize span for the current price as 1 (for the current day)
        span = 1

        # Pop elements from the stack while the price at the top is less than or equal to the current price
        while self.stack and self.stack[-1][0] <= price:
            # Add the span of the popped element to the current span
            span += self.stack.pop()[1]

        # Push the current price and its span onto the stack
        self.stack.append((price, span))

        return span

# Test cases


def test_stock_spanner():
    stockSpanner = StockSpanner()

    # Test case 1
    assert stockSpanner.next(100) == 1  # First day, span is 1
    assert stockSpanner.next(80) == 1   # Second day, price drops, span is 1
    # Third day, price drops again, span is 1
    assert stockSpanner.next(60) == 1
    # Fourth day, price rises, span is 2 (includes day 3 and 4)
    assert stockSpanner.next(70) == 2
    # Fifth day, price drops again, span is 1
    assert stockSpanner.next(60) == 1
    # Sixth day, price rises, span is 4 (includes days 2, 3, 4, and 6)
    assert stockSpanner.next(75) == 4
    # Seventh day, price rises, span is 6 (includes all previous days)
    assert stockSpanner.next(85) == 6

    print("All test cases passed!")


# Run the tests
test_stock_spanner()
