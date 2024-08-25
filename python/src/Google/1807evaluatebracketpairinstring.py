from typing import List


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        # Convert the knowledge list into a dictionary
        knowledge_dict = {k: v for k, v in knowledge}

        result = []
        i = 0
        while i < len(s):
            if s[i] == '(':
                i += 1
                key = []
                # Capture the key inside the brackets
                while s[i] != ')':
                    key.append(s[i])
                    i += 1
                # Move past the closing ')'
                i += 1
                key = ''.join(key)
                # Append the corresponding value or "?" if the key is not found
                result.append(knowledge_dict.get(key, '?'))
            else:
                # Append non-bracket characters directly to the result
                result.append(s[i])
                i += 1

        return ''.join(result)


# Example usage
solution = Solution()
s = "(name)is(age)yearsold"
knowledge = [["name", "bob"], ["age", "two"]]
print(solution.evaluate(s, knowledge))  # Output: "bobistwoyearsold"
