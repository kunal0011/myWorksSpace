from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0  # Initialize the count of $5 and $10 bills

        for bill in bills:
            if bill == 5:
                five += 1  # No change needed, increase the count of $5 bills
            elif bill == 10:
                if five > 0:
                    five -= 1  # Give one $5 as change
                    ten += 1   # Add one $10 bill to our count
                else:
                    return False  # Can't give change if no $5 bill
            elif bill == 20:
                if ten > 0 and five > 0:
                    ten -= 1  # Prefer to give one $10 and one $5 as change
                    five -= 1
                elif five >= 3:
                    five -= 3  # Give three $5 bills as change
                else:
                    return False  # Can't give change if we don't have enough bills

        return True  # If we get through all the customers, return True
