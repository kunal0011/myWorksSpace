from typing import List


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        in_block_comment = False
        result = []
        newline = ""

        for line in source:
            i = 0
            while i < len(line):
                if in_block_comment:
                    if line[i:i+2] == "*/":
                        in_block_comment = False
                        i += 1  # Skip the '/' part of '*/'
                    # Skip characters inside a block comment
                else:
                    if line[i:i+2] == "/*":
                        in_block_comment = True
                        i += 1  # Skip the '*' part of '/*'
                    elif line[i:i+2] == "//":
                        break  # Ignore the rest of the line
                    else:
                        newline += line[i]
                i += 1

            if not in_block_comment and newline:
                result.append(newline)
                newline = ""  # Reset for the next line

        return result
