class Solution:
    def peopleIndexes(self, favoriteCompanies: list[list[str]]) -> list[int]:
        sets = [set(fav) for fav in favoriteCompanies]
        result = []

        for i, current_set in enumerate(sets):
            if all(not current_set.issubset(other_set) for j, other_set in enumerate(sets) if i != j):
                result.append(i)

        return result
