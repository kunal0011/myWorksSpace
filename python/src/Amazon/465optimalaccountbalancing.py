"""
LeetCode 465 - Optimal Account Balancing

Problem Statement:
-----------------
You are given an array of transactions where transactions[i] = [fromi, toi, amounti] 
indicates that the person with ID = fromi gave amounti $ to the person with ID = toi.

Return the minimum number of transactions required to settle the debt.

Key Points:
----------
1. Need to find minimum number of transactions to settle all debts
2. Person IDs can be any non-negative integers
3. Amount is always positive
4. NP-hard problem requiring backtracking
5. Optimize by removing zero balances and grouping debts

Examples:
--------
Input: transactions = [[0,1,10], [2,0,5]]
Output: 2
Explanation:
Person #0 gave person #1 $10.
Person #2 gave person #0 $5.
Two transactions are needed. One way to settle the debt is person #1 pays person #0 and #2 $5 each.

Input: transactions = [[0,1,10], [1,0,1], [1,2,5], [2,0,5]]
Output: 1
Explanation:
Person #0 gave person #1 $10.
Person #1 gave person #0 $1.
Person #1 gave person #2 $5.
Person #2 gave person #0 $5.
After all transactions: #0 has net +$1, #1 has net -$4, #2 has net +$3
Only 1 transaction is needed: person #1 pays person #0 $4.

Constraints:
-----------
* 1 <= transactions.length <= 8
* transactions[i].length == 3
* 0 <= fromi, toi <= 20
* fromi != toi
* 1 <= amounti <= 100
"""

from typing import List
from collections import defaultdict


class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        """
        Find minimum number of transactions needed to settle all debts.
        
        Algorithm:
        1. Calculate net balance for each person
        2. Remove people with zero balance
        3. Use backtracking to try all possible debt settlements
        4. Optimize by settling opposite sign balances
        
        Time Complexity: O(n!) where n is number of people with non-zero balance
        Space Complexity: O(n) for recursion stack
        """
        # Calculate net balance for each person
        balance = defaultdict(int)
        for giver, receiver, amount in transactions:
            balance[giver] -= amount
            balance[receiver] += amount

        # Convert to list of non-zero balances
        debt = [b for b in balance.values() if b != 0]

        def settle_debt(start: int) -> int:
            """
            Recursive backtracking to find minimum transactions needed.
            
            Args:
                start: Starting index in debt array
            Returns:
                Minimum number of transactions needed from this state
            """
            # Skip settled (zero) debts
            while start < len(debt) and debt[start] == 0:
                start += 1
                
            # Base case: all debts settled
            if start == len(debt):
                return 0

            min_trans = float('inf')
            curr_debt = debt[start]
            
            # Try settling with each remaining person
            for i in range(start + 1, len(debt)):
                # Only try settling with opposite sign (can actually settle)
                if debt[i] * curr_debt < 0:
                    # Settle as much as possible
                    debt[i] += curr_debt
                    min_trans = min(min_trans, 1 + settle_debt(start + 1))
                    # Backtrack
                    debt[i] -= curr_debt

            return min_trans if min_trans != float('inf') else 0

        return settle_debt(0)


def test_min_transfers():
    """
    Test driver for optimal account balancing
    """
    test_cases = [
        (
            [[0,1,10], [2,0,5]],
            2,  # Basic case with three people
            "Two transactions needed: Person #1 pays $5 each to #0 and #2"
        ),
        (
            [[0,1,10], [1,0,1], [1,2,5], [2,0,5]],
            1,  # Can be settled with single transaction
            "One transaction: Person #1 pays $4 to Person #0"
        ),
        (
            [[0,1,1], [1,2,1], [2,3,1], [3,0,1]],
            0,  # Already settled (circular transactions)
            "No transactions needed - everyone gave and received equal amounts"
        ),
        (
            [[0,1,5], [1,2,5], [2,3,5]],
            3,  # Chain of debts
            "Three transactions needed to settle chain of debts"
        ),
        (
            [[0,1,2], [1,2,2], [2,3,2], [3,4,2], [4,0,2]],
            0,  # Circular with equal amounts
            "No transactions needed - circular with equal amounts"
        ),
        (
            [[0,1,100], [1,2,100], [2,0,100]],
            0,  # Large circular transactions
            "No transactions needed - large circular transactions cancel out"
        ),
        (
            [[0,1,1], [1,2,1], [2,0,1], [3,4,2], [4,5,2], [5,3,2]],
            0,  # Two separate circular groups
            "No transactions needed - two separate balanced groups"
        ),
        (
            [[0,1,10], [2,0,5], [3,0,5], [1,4,10]],
            3,  # Complex case requiring multiple settlements
            "Three transactions needed for optimal settlement"
        )
    ]
    
    solution = Solution()
    
    for i, (transactions, expected, description) in enumerate(test_cases, 1):
        result = solution.minTransfers(transactions)
        status = "PASSED" if result == expected else "FAILED"
        print(f"\nTest case {i}: {status}")
        print(f"Description: {description}")
        print("Transactions:")
        for t in transactions:
            print(f"Person #{t[0]} gave Person #{t[1]} ${t[2]}")
        print(f"Expected minimum transactions: {expected}")
        print(f"Got: {result}")
        if result != expected:
            print("Note: For failed cases, check if there's a more optimal solution")
        print("-" * 40)

if __name__ == "__main__":
    test_min_transfers()
