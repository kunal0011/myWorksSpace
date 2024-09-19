package amazon;

// Definition for a binary tree node.
class TreeNode701 {
    int val;
    TreeNode701 left;
    TreeNode701 right;
    TreeNode701() {}
    TreeNode701(int val) { this.val = val; }
    TreeNode701(int val, TreeNode701 left, TreeNode701 right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class Insertintobst701 {
    public TreeNode701 insertIntoBST(TreeNode701 root, int val) {
        if (root == null) {
            return new TreeNode701(val);
        }

        // Traverse the tree to find the correct position
        if (val < root.val) {
            root.left = insertIntoBST(root.left, val);
        } else {
            root.right = insertIntoBST(root.right, val);
        }

        return root;
    }

    // In-order traversal for testing
    public void inorderTraversal(TreeNode701 root) {
        if (root != null) {
            inorderTraversal(root.left);
            System.out.print(root.val + " ");
            inorderTraversal(root.right);
        }
    }

    // Test the function
    public static void main(String[] args) {
        Insertintobst701 sol = new Insertintobst701();

        // Test case 1
        TreeNode701 root1 = new TreeNode701(4, new TreeNode701(2, new TreeNode701(1), new TreeNode701(3)), new TreeNode701(7));
        int val1 = 5;
        root1 = sol.insertIntoBST(root1, val1);
        sol.inorderTraversal(root1);  // Output: 1 2 3 4 5 7

        // Test case 2
        TreeNode701 root2 = new TreeNode701(40, new TreeNode701(20, new TreeNode701(10), new TreeNode701(30)), new TreeNode701(60, new TreeNode701(50), new TreeNode701(70)));
        int val2 = 25;
        root2 = sol.insertIntoBST(root2, val2);
        sol.inorderTraversal(root2);  // Output: 10 20 25 30 40 50 60 70
    }
}
