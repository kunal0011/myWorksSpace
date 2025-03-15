"""
LeetCode 901: Online Stock Span

Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of consecutive days 
(starting from today and going backward) for which the stock price was less than or equal to today's price.

Implement the StockSpanner class:
- StockSpanner() Initializes the object of the class
- int next(int price) Returns the span of the stock's price given that today's price is 'price'

Constraints:
- 1 <= price <= 10^5
- At most 10^4 calls will be made to next
"""

class StockSpanner:
    def __init__(self):
        self.stack = []  # Stack of (price, span) pairs
        self.day = 0    # Keep track of days for validation
        
    def next(self, price: int) -> int:
        self.day += 1
        span = 1
        
        # Pop all prices less than or equal to current price
        while self.stack and self.stack[-1][0] <= price:
            prev_price, prev_span = self.stack.pop()
            span += prev_span
            
        self.stack.append((price, span))
        return span

def validate_price(price: int) -> bool:
    """Validate price according to constraints"""
    return 1 <= price <= 10**5

def test_stock_spanner():
    """Test function for Online Stock Span"""
    test_cases = [
        # (prices, expected_spans)
        ([100, 80, 60, 70, 60, 75, 85], [1, 1, 1, 2, 1, 4, 6]),
        ([10, 20, 30, 40, 50], [1, 2, 3, 4, 5]),
        ([90, 80, 70, 60, 50], [1, 1, 1, 1, 1]),
        ([100, 100, 100], [1, 2, 3]),
        ([70, 60, 75, 85, 85, 90], [1, 1, 2, 3, 4, 6])
    ]
    
    for i, (prices, expected) in enumerate(test_cases, 1):
        spanner = StockSpanner()
        results = []
        
        print(f"\nTest case {i}:")
        print("Day  Price  Span  Stack State")
        print("-" * 40)
        
        for day, price in enumerate(prices, 1):
            is_valid = validate_price(price)
            span = spanner.next(price)
            results.append(span)
            
            # Visualize the state
            print(f"{day:3d}  {price:5d}  {span:4d}   {spanner.stack}")
            
            if not is_valid:
                print(f"Warning: Invalid price {price} on day {day}")
        
        # Test results
        success = results == expected
        print(f"\nPrices: {prices}")
        print(f"Expected spans: {expected}")
        print(f"Got spans: {results}")
        print(f"Test passed: {'✓' if success else '✗'}")
        
        # Additional analysis
        print(f"Maximum span: {max(results)}")
        print(f"Average span: {sum(results)/len(results):.2f}")
        print(f"Monotonic days: {sum(1 for i in range(1, len(results)) if results[i] > results[i-1])}")

if __name__ == "__main__":
    test_stock_spanner()
