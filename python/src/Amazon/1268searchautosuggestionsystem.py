from bisect import bisect_left


class Solution:
    def suggestedProducts(self, products, searchWord):
        # Sort the products lexicographically
        products.sort()
        result = []
        prefix = ""

        # Iterate over each character in searchWord
        for char in searchWord:
            prefix += char
            # Find the insertion point using binary search
            idx = bisect_left(products, prefix)

            # Collect up to 3 suggestions that start with the prefix
            suggestions = []
            for i in range(idx, min(len(products), idx + 3)):
                if products[i].startswith(prefix):
                    suggestions.append(products[i])
                else:
                    break
            result.append(suggestions)

        return result
