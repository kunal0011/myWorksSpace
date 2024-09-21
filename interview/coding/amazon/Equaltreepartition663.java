package amazon;

// Definition for a binary tree node.
class TreeNode663 {
    int val;
    TreeNode663 left;
    TreeNode663 right;
    TreeNode663() {}
    TreeNode663(int val) { this.val = val; }
    TreeNode663(int val, TreeNode663 left, TreeNode663 right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class Equaltreepartition663 {
    private boolean found = false;

    public boolean checkEqualTree(TreeNode663 root) {
        int total = totalSum(root);
        if (total % 2 != 0) {
            return false;  // If total sum is odd, can't split into two equal parts
        }
        dfs(root, root, total);
        return found;
    }

    // Helper function to calculate the total sum of the tree
    private int totalSum(TreeNode663 node) {
        if (node == null) {
            return 0;
        }
        return node.val + totalSum(node.left) + totalSum(node.right);
    }

    // DFS to check subtree sums
    private int dfs(TreeNode663 node, TreeNode663 root, int total) {
        if (node == null) {
            return 0;
        }
        int currentSum = node.val + dfs(node.left, root, total) + dfs(node.right, root, total);
        if (currentSum * 2 == total && node != root) {
            found = true;
        }
        return currentSum;
    }

    // Test cases
    public static void main(String[] args) {
        Equaltreepartition663 sol = new Equaltreepartition663();

        // Test case 1
        TreeNode663 root1 = new TreeNode663(5,
                new TreeNode663(10),
                new TreeNode663(10, new TreeNode663(2), new TreeNode663(3)));
        System.out.println(sol.checkEqualTree(root1));  // Output: True

        // Test case 2
        TreeNode663 root2 = new TreeNode663(1,
                new TreeNode663(2),
                new TreeNode663(10, new TreeNode663(2), new TreeNode663(20)));
        System.out.println(sol.checkEqualTree(root2));  // Output: False
    }
}
