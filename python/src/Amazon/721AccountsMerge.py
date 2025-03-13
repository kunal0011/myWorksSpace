"""
LeetCode 721: Accounts Merge

Given a list of accounts where each element accounts[i] is a list of strings, where the first element 
accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there 
is some common email to both accounts. Note that even if two accounts have the same name, they may 
belong to different people as people could have the same name. A person can have any number of accounts 
initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each 
account is the name, and the rest of the elements are emails in sorted order.
"""

from collections import defaultdict
from typing import List

class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = defaultdict(int)

    def find(self, x: str) -> str:
        if x not in self.parent:
            self.parent[x] = x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x: str, y: str) -> None:
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            # Union by rank
            if self.rank[rootX] < self.rank[rootY]:
                rootX, rootY = rootY, rootX
            self.parent[rootY] = rootX
            if self.rank[rootX] == self.rank[rootY]:
                self.rank[rootX] += 1

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind()
        email_to_name = {}
        
        # Step 1: Build Union-Find structure
        for account in accounts:
            name = account[0]
            # Optimize by only processing emails if there are any
            if len(account) > 1:
                first_email = account[1]
                email_to_name[first_email] = name
                for email in account[2:]:
                    email_to_name[email] = name
                    uf.union(first_email, email)

        # Step 2: Group emails by their representative
        email_groups = defaultdict(set)
        for email in email_to_name:
            root_email = uf.find(email)
            email_groups[root_email].add(email)

        # Step 3: Format result
        return [[email_to_name[root]] + sorted(emails) 
                for root, emails in email_groups.items()]

def test_accounts_merge():
    """Test function for accountsMerge with multiple test cases"""
    test_cases = [
        # Test case 1: Basic merge
        (
            [
                ["John", "johnsmith@mail.com", "john00@mail.com"],
                ["John", "johnnybravo@mail.com"],
                ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                ["Mary", "mary@mail.com"]
            ],
            [
                ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
                ["John", "johnnybravo@mail.com"],
                ["Mary", "mary@mail.com"]
            ]
        ),
        # Test case 2: Same names, different people
        (
            [
                ["David", "David0@m.co", "David1@m.co"],
                ["David", "David3@m.co", "David4@m.co"],
                ["David", "David4@m.co", "David5@m.co"],
                ["David", "David2@m.co", "David3@m.co"],
                ["David", "David1@m.co", "David2@m.co"]
            ],
            [
                ["David", "David0@m.co", "David1@m.co", "David2@m.co", 
                 "David3@m.co", "David4@m.co", "David5@m.co"]
            ]
        ),
        # Test case 3: Single account
        (
            [["Alex", "Alex@m.co", "Alex@m.co"]],
            [["Alex", "Alex@m.co"]]
        )
    ]
    
    solution = Solution()
    for i, (input_accounts, expected) in enumerate(test_cases, 1):
        result = solution.accountsMerge(input_accounts)
        success = sorted(str(result)) == sorted(str(expected))
        print(f"\nTest case {i}:")
        print(f"Input: {input_accounts}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"{'✓ Passed' if success else '✗ Failed'}")

if __name__ == "__main__":
    test_accounts_merge()
