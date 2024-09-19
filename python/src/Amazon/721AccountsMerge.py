from collections import defaultdict


class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootX] = rootY


class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        uf = UnionFind()
        email_to_name = {}

        # Initialize Union-Find structure and map emails to names
        for account in accounts:
            name = account[0]
            first_email = account[1]
            if first_email not in uf.parent:
                # Initialize email in union-find
                uf.parent[first_email] = first_email
            email_to_name[first_email] = name  # Map email to person's name

            for email in account[1:]:
                if email not in uf.parent:
                    uf.parent[email] = email  # Initialize email in union-find
                email_to_name[email] = name  # Map email to person's name
                uf.union(first_email, email)  # Union emails of the same person

        # Group emails by their root parent (i.e., their representative)
        merged_accounts = defaultdict(list)
        for email in uf.parent:
            root_email = uf.find(email)
            merged_accounts[root_email].append(email)

        # Prepare the result with sorted emails and corresponding names
        result = []
        for emails in merged_accounts.values():
            result.append([email_to_name[emails[0]]] + sorted(emails))

        return result


# Test the function
if __name__ == "__main__":
    sol = Solution()

    accounts1 = [
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["John", "johnnybravo@mail.com"],
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["Mary", "mary@mail.com"]
    ]
    print(sol.accountsMerge(accounts1))
    # Output:
    # [
    #   ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
    #   ["John", "johnnybravo@mail.com"],
    #   ["Mary", "mary@mail.com"]
    # ]
