class Solution:
    def simplifyPath(self, path: str) -> str:
        components = path.split('/')

    # Initialize a stack to keep track of the canonical path
        stack = []

        # Process each component
        for component in components:
            if component == '' or component == '.':
                # Ignore empty components and single "."
                continue
            elif component == '..':
                # Move up one directory level
                if stack:
                    stack.pop()
            else:
                # Valid directory name
                stack.append(component)

        # Construct the canonical path
        canonical_path = '/' + '/'.join(stack)

        # Handle case where canonical_path is just "/"
        if canonical_path == '/':
            return canonical_path
        else:
            return canonical_path.rstrip('/')


if __name__ == '__main__':

    s = Solution()

    print(s.simplifyPath("/home/user/Documents/../Pictures"))
