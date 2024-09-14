class Solution:
    def processQueries(self, queries, m):
        perm = list(range(1, m + 1))
        result = []

        for q in queries:
            index = perm.index(q)
            result.append(index)
            perm.insert(0, perm.pop(index))

        return result
