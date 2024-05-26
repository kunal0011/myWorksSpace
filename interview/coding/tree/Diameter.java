package tree;

// Definition for a binary tree node.


public class Diameter {
    // Global variable to track the maximum diameter
    private int maxDiameter = 0;

    public int diameterOfBinaryTree(TreeNode root) {
        // Start the recursion from the root
        height(root);
        return maxDiameter;
    }

    // Helper function to compute the height of a subtree and update the diameter
    private int height(TreeNode node) {
        if (node == null) {
            return 0;
        }

        // Recursively compute the height of the left and right subtrees
        int leftHeight = height(node.left);
        int rightHeight = height(node.right);

        // Update the diameter at the current node
        maxDiameter = Math.max(maxDiameter, leftHeight + rightHeight);

        // Return the height of the subtree rooted at the current node
        return Math.max(leftHeight, rightHeight) + 1;
    }

    public static void main(String[] args) {
        // Create a sample binary tree
        //         1
        //        / \
        //       2   3
        //      / \
        //     4   5
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);

        // Instantiate the Solution class
        Diameter solution = new Diameter();

        // Calculate the diameter of the binary tree
        int diameter = solution.diameterOfBinaryTree(root);

        // Print the result
        System.out.println("Diameter of the binary tree: " + diameter);
    }
}
