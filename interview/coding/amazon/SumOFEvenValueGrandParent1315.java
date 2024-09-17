package amazon;

// Definition for a binary tree node.
class TreeNode1315 {
    int val;
    TreeNode1315 left;
    TreeNode1315 right;

    TreeNode1315() {}
    TreeNode1315(int val) { this.val = val; }
    TreeNode1315(int val, TreeNode1315 left, TreeNode1315 right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class SumOFEvenValueGrandParent1315 {
    public int sumEvenGrandparent(TreeNode1315 root) {
        return dfs(root, null, null);
    }

    private int dfs(TreeNode1315 node, TreeNode1315 parent, TreeNode1315 grandparent) {
        if (node == null) {
            return 0;
        }

        // Initialize sum to 0
        int sum = 0;

        // If grandparent exists and its value is even, add the node's value to the sum
        if (grandparent != null && grandparent.val % 2 == 0) {
            sum += node.val;
        }

        // Recursively sum for the left and right children
        sum += dfs(node.left, node, parent);
        sum += dfs(node.right, node, parent);

        return sum;
    }

    // Testing
    public static void main(String[] args) {
        TreeNode1315 root = new TreeNode1315(6,
                new TreeNode1315(7,
                        new TreeNode1315(2, new TreeNode1315(9), null),
                        new TreeNode1315(7, new TreeNode1315(1), new TreeNode1315(4))),
                new TreeNode1315(8,
                        new TreeNode1315(1),
                        new TreeNode1315(3)));

        SumOFEvenValueGrandParent1315 solution = new SumOFEvenValueGrandParent1315();
        System.out.println("Java Test Result: " + solution.sumEvenGrandparent(root));  // Output: 18
    }
}
