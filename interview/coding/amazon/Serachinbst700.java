package amazon;

// Definition for a binary tree node.
class TreeNode700 {
    int val;
    TreeNode700 left;
    TreeNode700 right;
    TreeNode700() {}
    TreeNode700(int val) { this.val = val; }
    TreeNode700(int val, TreeNode700 left, TreeNode700 right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class Serachinbst700 {
    public TreeNode700 searchBST(TreeNode700 root, int val) {
        // Base case: root is null or we find the node with the value
        if (root == null || root.val == val) {
            return root;
        }

        // If the value is less than the root's value, search the left subtree
        if (val < root.val) {
            return searchBST(root.left, val);
        }
        // Otherwise, search the right subtree
        return searchBST(root.right, val);
    }

    // In-order traversal for testing
    public void inorderTraversal(TreeNode700 root) {
        if (root != null) {
            inorderTraversal(root.left);
            System.out.print(root.val + " ");
            inorderTraversal(root.right);
        }
    }

    // Test the function
    public static void main(String[] args) {
        Serachinbst700 sol = new Serachinbst700();

        // Test case 1
        TreeNode700 root1 = new TreeNode700(4, new TreeNode700(2, new TreeNode700(1), new TreeNode700(3)), new TreeNode700(7));
        int val1 = 2;
        TreeNode700 result1 = sol.searchBST(root1, val1);
        sol.inorderTraversal(result1);  // Output: 1 2 3

        // Test case 2
        TreeNode700 root2 = new TreeNode700(4, new TreeNode700(2, new TreeNode700(1), new TreeNode700(3)), new TreeNode700(7));
        int val2 = 5;
        TreeNode700 result2 = sol.searchBST(root2, val2);
        sol.inorderTraversal(result2);  // Output: (empty)
    }
}

