from typing import List


class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        def buildStrobogrammatic(n, m):
            if n == 0:
                return [""]
            if n == 1:
                return ["0", "1", "8"]

            result = []
            smallerNumbers = buildStrobogrammatic(n - 2, m)

            for num in smallerNumbers:
                if n != m:  # Avoid adding '0' at the beginning of the number
                    result.append("0" + num + "0")
                result.append("1" + num + "1")
                result.append("6" + num + "9")
                result.append("8" + num + "8")
                result.append("9" + num + "6")

            return result

        return buildStrobogrammatic(n, n)
