class Solution:
    def minTransfers(self, transactions: list[list[int]]) -> int:
        # Step 1: Calculate net balances
        balance = {}

        for t in transactions:
            giver, receiver, amount = t
            balance[giver] = balance.get(giver, 0) - amount
            balance[receiver] = balance.get(receiver, 0) + amount

        # Step 2: Remove zero balances (people who have no net debt)
        debt = [b for b in balance.values() if b != 0]

        # Backtracking function to minimize transactions
        def settle(debt, start):
            # Skip already settled debts
            while start < len(debt) and debt[start] == 0:
                start += 1
            if start == len(debt):
                return 0

            min_transactions = float('inf')
            for i in range(start + 1, len(debt)):
                if debt[i] * debt[start] < 0:  # opposite signs, can settle
                    # Settle debt[start] with debt[i]
                    debt[i] += debt[start]
                    min_transactions = min(
                        min_transactions, 1 + settle(debt, start + 1))
                    # Backtrack
                    debt[i] -= debt[start]

            return min_transactions

        return settle(debt, 0)


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    transactions1 = [[0, 1, 10], [2, 0, 5]]
    print(sol.minTransfers(transactions1))  # Expected output: 2

    # Test case 2
    transactions2 = [[0, 1, 10], [1, 2, 5], [2, 0, 5]]
    print(sol.minTransfers(transactions2))  # Expected output: 1
