package amazon;

// Definition for a binary tree node.
class TreeNode979
{
    int val;
    TreeNode979 left;
    TreeNode979 right;
    TreeNode979() {}
    TreeNode979(int val) { this.val = val; }
    TreeNode979(int val, TreeNode979 left, TreeNode979 right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class DistributeCoininBT979 {
    private int moves = 0;

    public int distributeCoins(TreeNode979 root) {
        postOrder(root);
        return moves;
    }

    private int postOrder(TreeNode979 node) {
        if (node == null) {
            return 0;
        }

        // Post-order traversal: process left and right children first
        int leftBalance = postOrder(node.left);
        int rightBalance = postOrder(node.right);

        // Calculate the balance of the current node
        int balance = node.val - 1 + leftBalance + rightBalance;

        // The number of moves is increased by the absolute value of the balance at this node
        moves += Math.abs(balance);

        return balance;
    }

    // Testing
    public static void main(String[] args) {
        DistributeCoininBT979 solution = new DistributeCoininBT979();
        TreeNode979 root = new TreeNode979(3);
        root.left = new TreeNode979(0);
        root.right = new TreeNode979(0);
        System.out.println("Java Test Result: " + solution.distributeCoins(root));  // Output: 2
    }
}
