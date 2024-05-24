package tree;


public class PathSumRootToLeaf {
    public boolean hasPathSum(TreeNode root, int sum) {
        // Base case: if the tree is empty
        if (root == null) {
            return false;
        }

        // Check if we are at a leaf node
        if (root.left == null && root.right == null) {
            return sum == root.val;
        }

        // Subtract the current node's value from the sum and check the subtrees
        int remainingSum = sum - root.val;
        return hasPathSum(root.left, remainingSum) || hasPathSum(root.right, remainingSum);
    }

    public static void main(String[] args) {
        PathSumRootToLeaf solution = new PathSumRootToLeaf  ();

        // Creating a sample tree:
        //         5
        //        / \
        //       4   8
        //      /   / \
        //     11  13  4
        //    /  \      \
        //   7    2      1
        TreeNode root = new TreeNode(5);
        root.left = new TreeNode(4);
        root.right = new TreeNode(8);
        root.left.left = new TreeNode(11);
        root.left.left.left = new TreeNode(7);
        root.left.left.right = new TreeNode(2);
        root.right.left = new TreeNode(13);
        root.right.right = new TreeNode(4);
        root.right.right.right = new TreeNode(1);

        int sum = 22;
        boolean result = solution.hasPathSum(root, sum);
        System.out.println("Does the tree have a root-to-leaf path with sum " + sum + "? " + result);
    }
}
