class Solution:
    def findSolution(self, customFunction, z):
        results = []
        x, y = 1, 1000

        while x <= 1000 and y > 0:
            result = customFunction.f(x, y)
            if result == z:
                results.append([x, y])
                x += 1
                y -= 1
            elif result < z:
                x += 1
            else:
                y -= 1

        return results
