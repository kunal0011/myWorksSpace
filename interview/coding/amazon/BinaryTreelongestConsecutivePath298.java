package amazon;
class TreeNode298 {
    int val;
    TreeNode298 left;
    TreeNode298 right;
    TreeNode298() {}
    TreeNode298(int val) { this.val = val; }
    TreeNode298(int val, TreeNode298 left, TreeNode298 right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class BinaryTreelongestConsecutivePath298 {
    public int longestConsecutive(TreeNode298 root) {
        return dfs(root, null, 0);
    }

    private int dfs(TreeNode298 node, TreeNode298 parent, int length) {
        if (node == null) {
            return length;
        }

        if (parent != null && node.val == parent.val + 1) {
            length++;
        } else {
            length = 1;
        }

        int left = dfs(node.left, node, length);
        int right = dfs(node.right, node, length);

        return Math.max(length, Math.max(left, right));
    }
}
