package tree;

public class MaxPathSum {
    // Global variable to store the maximum path sum
    private int maxSum = Integer.MIN_VALUE;

    public int maxPathSum(TreeNode root) {
        // Start the recursion from the root
        helper(root);
        return maxSum;
    }

    // Helper function to compute the maximum path sum
    private int helper(TreeNode node) {
        if (node == null) {
            return 0;
        }

        // Recursively get the maximum path sum of the left and right subtrees
        int leftMax = Math.max(helper(node.left), 0);
        int rightMax = Math.max(helper(node.right), 0);

        // Compute the path sum through the current node
        int currentSum = node.val + leftMax + rightMax;

        // Update the global maximum path sum
        maxSum = Math.max(maxSum, currentSum);

        // Return the maximum path sum "starting" from the current node
        return node.val + Math.max(leftMax, rightMax);
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
        MaxPathSum solution = new MaxPathSum();

        // Calculate the maximum path sum of the binary tree
        int maxPathSum = solution.maxPathSum(root);

        // Print the result
        System.out.println("Maximum path sum of the binary tree: " + maxPathSum);
    }
}
