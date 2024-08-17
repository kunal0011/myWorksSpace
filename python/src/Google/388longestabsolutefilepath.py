class Solution:
    def lengthLongestPath(self, input: str) -> int:
        max_length = 0
        # Dictionary to store the length of path at each level
        path_length = {0: 0}

        for line in input.splitlines():
            name = line.lstrip('\t')
            level = len(line) - len(name)  # Number of '\t' indicates the level

            if '.' in name:
                # It's a file, calculate the total length
                max_length = max(max_length, path_length[level] + len(name))
            else:
                # It's a directory, update the current path length
                path_length[level + 1] = path_length[level] + \
                    len(name) + 1  # +1 for the '/'

        return max_length
