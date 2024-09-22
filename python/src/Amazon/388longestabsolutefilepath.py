class Solution:
    def lengthLongestPath(self, input: str) -> int:
        # Stack to store the current path length at each depth
        stack = []
        max_len = 0

        # Split the input by newlines to process each line (directory or file)
        for line in input.splitlines():
            # Count the depth of the current directory or file (number of tabs)
            depth = line.count('\t')
            # Remove the tabs to get the actual name
            name = line.replace('\t', '')

            # If stack is larger than current depth, pop the stack to move back to the parent directory
            while len(stack) > depth:
                stack.pop()

            if '.' in name:
                # If it's a file, calculate the total length of the path
                current_length = len(name) + sum(stack) + len(stack)
                max_len = max(max_len, current_length)
            else:
                # If it's a directory, push its length to the stack
                stack.append(len(name))

        return max_len


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    input1 = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
    print(sol.lengthLongestPath(input1))  # Output: 20

    # Test case 2
    input2 = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext\n\tsubdir3"
    print(sol.lengthLongestPath(input2))  # Output: 20

    # Test case 3
    input3 = "dir\n\tsubdir1\n\t\tfile1.ext\n\tsubdir2\n\t\tfile2.ext"
    print(sol.lengthLongestPath(input3))  # Output: 21
