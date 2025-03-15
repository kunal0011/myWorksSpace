"""
LeetCode 860: Lemonade Change

At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you
and order one at a time. Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.
You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

Return true if you can provide every customer with the correct change, or false otherwise.

Constraints:
- 1 <= bills.length <= 10^5
- bills[i] is either 5, 10, or 20
"""

from typing import List
from collections import Counter

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if not five:  # Need $5 for change
                    return False
                five -= 1
                ten += 1
            else:  # bill == 20
                if ten and five:  # Prefer $10 + $5 combination
                    ten -= 1
                    five -= 1
                elif five >= 3:  # Otherwise use three $5
                    five -= 3
                else:
                    return False
        return True

def validate_bills(bills: List[int]) -> bool:
    """Validate input according to constraints"""
    if not 1 <= len(bills) <= 10**5:
        return False
    return all(bill in (5, 10, 20) for bill in bills)

def test_lemonade_change():
    """Test function for Lemonade Change"""
    test_cases = [
        ([5,5,5,10,20], True),
        ([5,5,10,10,20], False),
        ([5,5,10], True),
        ([10,10], False),
        ([5,5,5,5,20,20,5,5,20,5], False),
        ([5,5,5,10,5,5,10,20,20,20], False)
    ]
    
    solution = Solution()
    
    for i, (bills, expected) in enumerate(test_cases, 1):
        is_valid = validate_bills(bills)
        result = solution.lemonadeChange(bills)
        
        print(f"\nTest case {i}:")
        print(f"Customer bills: {bills}")
        
        # Count bills
        bill_count = Counter(bills)
        print(f"Bill distribution: $5: {bill_count[5]}, $10: {bill_count[10]}, $20: {bill_count[20]}")
        
        # Calculate total money received
        total = sum(bills)
        print(f"Total received: ${total}")
        print(f"Total customers: {len(bills)}")
        
        print(f"Can make change: {'✓' if result else '✗'}")
        print(f"Expected result: {'✓' if expected else '✗'}")
        print(f"Valid input: {'✓' if is_valid else '✗'}")
        print(f"Test passed: {'✓' if result == expected else '✗'}")

if __name__ == "__main__":
    test_lemonade_change()
