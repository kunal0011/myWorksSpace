class Solution:
    def findLeaves(self, root):
        res = []

        def dfs(node):
            if not node:
                return -1
            left = dfs(node.left)
            right = dfs(node.right)
            height = max(left, right) + 1

            if height == len(res):
                res.append([])

            res[height].append(node.val)
            return height

        dfs(root)
        return res
