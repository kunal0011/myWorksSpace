package amazon;

// Definition for a binary tree node.
 class TreeNode1022 {
    int val;
    TreeNode1022 left;
    TreeNode1022 right;
    TreeNode1022() {}
    TreeNode1022(int val) { this.val = val; }
    TreeNode1022(int val, TreeNode1022 left, TreeNode1022 right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

    public class Sumroottoleaf1022 {
    private static final int MOD = 1_000_000_007;

    public int sumRootToLeaf(TreeNode1022 root) {
        return dfs(root, 0);
    }

    // DFS helper function
    private int dfs(TreeNode1022 node, int currentValue) {
        if (node == null) {
            return 0;
        }

        // Update the current value (shift left and add current node's value)
        currentValue = (currentValue << 1) | node.val;

        // If it's a leaf node, return the current binary number
        if (node.left == null && node.right == null) {
            return currentValue;
        }

        // Recur for left and right children
        int leftSum = dfs(node.left, currentValue);
        int rightSum = dfs(node.right, currentValue);

        return (leftSum + rightSum) % MOD;
    }

    // Testing
    public static void main(String[] args) {
        TreeNode1022 root = new TreeNode1022(1);
        root.left = new TreeNode1022(0);
        root.right = new TreeNode1022(1);
        root.left.left = new TreeNode1022(0);
        root.left.right = new TreeNode1022(1);
        root.right.left = new TreeNode1022(0);
        root.right.right = new TreeNode1022(1);

        Sumroottoleaf1022 solution = new Sumroottoleaf1022();
        System.out.println("Java Test Result: " + solution.sumRootToLeaf(root));  // Output: 22
    }
}
